import json
import os
import time
import requests
import logging
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re
from typing import List, Dict, Tuple, Any, Optional
from dataclasses import dataclass
from pathlib import Path
from pydantic import BaseModel, Field
from openai import OpenAI
import instructor
from langsmith import traceable
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.schema import Document



# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Enhanced imports with fallback options
try:
    from langchain_openai import ChatOpenAI
    from langsmith import traceable, Client
    LANGCHAIN_AVAILABLE = True
except ImportError:
    print("Warning: langchain_openai not available.")
    LANGCHAIN_AVAILABLE = False

try:
    from langchain_community.document_loaders import WebBaseLoader
    LANGCHAIN_WEB_AVAILABLE = True
except ImportError:
    print("Warning: langchain_community not available for web loading.")
    LANGCHAIN_WEB_AVAILABLE = False

try:
    import selenium
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import TimeoutException, WebDriverException
    SELENIUM_AVAILABLE = True
except ImportError:
    print("Warning: Selenium not available. Dynamic content may not load properly.")
    SELENIUM_AVAILABLE = False

# Docling imports (assuming docling is available)
try:
    from docling.document_converter import DocumentConverter
    from docling.datamodel.base_models import InputFormat
    DOCLING_AVAILABLE = True
except ImportError:
    print("Warning: Docling not available. Please install docling for PDF processing.")
    DOCLING_AVAILABLE = False

# --- Pydantic Models for Semantic Sectioning ---
class DocumentSection(BaseModel):
    title: str = Field(description="main topic of this section of the document (very descriptive)")
    start_index: int = Field(description="line number where the section begins (inclusive)")

class StructuredDocument(BaseModel):
    """obtains meaningful sections, each centered around a single concept/topic"""
    sections: List[DocumentSection] = Field(description="an ordered list of sections of the document")

class Line(BaseModel):
    content: str
    element_type: str = "NarrativeText"
    page_number: Optional[int] = None
    is_visual: bool = False

class Section(BaseModel):
    title: str
    content: str
    start: int
    end: int

# --- System Prompt for Semantic Sectioning ---
SYSTEM_PROMPT = """
Read the document below and extract a StructuredDocument object from it where each section of the document is centered around a single concept/topic. Whenever possible, your sections (and section titles) should match up with the natural sections of the document (i.e. Introduction, Conclusion, References, etc.). Sections can vary in length, but should generally be anywhere from a few paragraphs to a few pages long.

Each line of the document is marked with its line number in square brackets (e.g. [1], [2], [3], etc). Use the line numbers to indicate section start.

The start line numbers will be treated as inclusive. For example, if the first line of a section is line 5, the start_index should be 5. Your goal is to find the starting line number of a given section, where a section is a group of lines that are thematically related.

The first section must start at the first line number of the document window provided ({start_line} in this case). The sections MUST cover the entire document window, and they MUST be in order.

Section titles should be descriptive enough such that a person who is just skimming over the section titles and not actually reading the document can get a clear idea of what each section is about.

Note: the document provided to you may just be an excerpt from a larger document, rather than a complete document. Therefore, you can't always assume, for example, that the first line of the document is the beginning of the Introduction section and the last line is the end of the Conclusion section (if those section are even present).
"""   

@dataclass
class ScrapingStrategy:
    """Configuration for different scraping strategies"""
    name: str
    wait_time: int = 5
    scroll_strategy: str = "none"  # none, simple, progressive, infinite
    content_selectors: List[str] = None
    javascript_required: bool = False
    custom_logic: Optional[callable] = None
    
    def __post_init__(self):
        if self.content_selectors is None:
            self.content_selectors = []

@dataclass
class APIEndpoint:
    method: str
    endpoint: str
    description: str = ""
    entities: List[str] = None
    kpis: List[str] = None  # Added KPIs field
    confidence_score: float = 0.0
    
    def __post_init__(self):
        if self.entities is None:
            self.entities = []
        if self.kpis is None:
            self.kpis = []

class SemanticSectioner:
    def __init__(self, api_key: str, model: str = "gpt-4.1-mini-2025-04-14"):
        """
        Initialize the semantic sectioner.
        
        Args:
            api_key: OpenAI API key
            model: OpenAI model to use
        """
        self.api_key = api_key
        self.model = model
        self.client = instructor.from_openai(OpenAI(api_key=api_key))
    
    def str_to_lines(self, document: str, max_line_length: int = 200) -> List[Line]:
        """Convert document string to list of Line objects."""
        document_lines = []
        lines = document.split("\n")
        
        for line in lines:
            if len(line) <= max_line_length:
                document_lines.append(Line(
                    content=line,
                    element_type="NarrativeText",
                    page_number=None,
                    is_visual=False
                ))
            else:
                # Split long lines at word boundaries
                words = line.split()
                current_line = []
                current_length = 0
                
                for word in words:
                    if current_length + len(word) + 1 <= max_line_length or not current_line:
                        current_line.append(word)
                        current_length += len(word) + 1
                    else:
                        document_lines.append(Line(
                            content=" ".join(current_line),
                            element_type="NarrativeText",
                            page_number=None,
                            is_visual=False
                        ))
                        current_line = [word]
                        current_length = len(word)
                
                if current_line:
                    document_lines.append(Line(
                        content=" ".join(current_line),
                        element_type="NarrativeText",
                        page_number=None,
                        is_visual=False
                    ))
        
        return document_lines
    
    def create_document_windows(self, document_lines: List[Line], max_characters_per_window: int = 20000) -> List[Tuple[int, int]]:
        """Divide document into processing windows."""
        windows = []
        doc_length = len(document_lines)
        
        if doc_length == 0:
            return windows
        
        window_start = 0
        character_count = 0
        
        for i in range(doc_length):
            line = document_lines[i].content
            character_count += len(line)
            
            # Check if we've reached the max characters or end of document
            if character_count >= 0.9 * max_characters_per_window or i == doc_length - 1:
                windows.append((window_start, i))
                window_start = i + 1
                character_count = 0
        
        # Handle partial window at the end
        if window_start < doc_length:
            windows.append((window_start, doc_length - 1))
        
        logger.info(f"Created {len(windows)} document windows")
        return windows
    
    def get_document_text_for_window(self, document_lines: List[Line], window_start: int, window_end: int) -> str:
        """Prepare text for a specific window with line numbers."""
        document_with_line_numbers = ""
        for i in range(window_start, min(window_end + 1, len(document_lines))):
            line = document_lines[i].content
            document_with_line_numbers += f"[{i}] {line}\n"
        return document_with_line_numbers
    
    def get_structured_document_for_window(self, window_text: str, first_line_number: int) -> StructuredDocument:
        """Send window to LLM and get structured sections."""
        formatted_system_prompt = SYSTEM_PROMPT.format(start_line=first_line_number)
        
        return self.client.chat.completions.create(
            model=self.model,
            response_model=StructuredDocument,
            max_tokens=4000,
            temperature=0.0,
            messages=[
                {
                    "role": "system",
                    "content": formatted_system_prompt,
                },
                {
                    "role": "user",
                    "content": window_text,
                },
            ],
        )
    
    def process_window_with_retries(self, window_text: str, first_line_number: int, max_retries: int = 3) -> Optional[StructuredDocument]:
        """Process window with retry logic."""
        for attempt in range(max_retries):
            try:
                logger.info(f"Processing window starting at line {first_line_number} (attempt {attempt+1}/{max_retries})")
                result = self.get_structured_document_for_window(window_text, first_line_number)
                logger.info(f"Successfully processed window at line {first_line_number}")
                return result
            except Exception as e:
                logger.warning(f"Attempt {attempt + 1}/{max_retries} failed for window at line {first_line_number}: {e}")
                if attempt < max_retries - 1:
                    time.sleep(2 * (attempt + 1))  # Exponential backoff
                else:
                    logger.error(f"All {max_retries} attempts failed for window at line {first_line_number}")
                    return None
        return None
    
    def validate_and_fix_window_sections(self, sections: List[DocumentSection], window_start: int, window_end: int, document_length: int) -> List[DocumentSection]:
        """Validate and fix sections for a window."""
        if not sections:
            return [DocumentSection(title=f"Window {window_start}-{window_end}", start_index=window_start)]
        
        # Remove duplicates and sort
        seen_indices = set()
        unique_sections = []
        for s in sections:
            if s.start_index not in seen_indices:
                seen_indices.add(s.start_index)
                unique_sections.append(s)
        
        sections = sorted(unique_sections, key=lambda x: x.start_index)
        
        # Fix section indices
        fixed_sections = []
        last_start = window_start - 1
        
        for i, section in enumerate(sections):
            if i == 0:
                # First section should start at window_start
                start = window_start
            else:
                # Subsequent sections should be after prior section
                start = max(last_start + 1, min(section.start_index, window_end))
            
            # Skip if beyond window or document bounds
            if start > window_end or start >= document_length:
                continue
            
            fixed_sections.append(DocumentSection(
                title=section.title,
                start_index=start
            ))
            last_start = start
        
        if not fixed_sections:
            fixed_sections.append(DocumentSection(
                title=f"Window {window_start}-{window_end}",
                start_index=window_start
            ))
        
        return fixed_sections
    
    def merge_sections_across_windows(self, all_window_sections: List[List[DocumentSection]]) -> List[DocumentSection]:
        """Merge sections from different windows."""
        if not all_window_sections:
            return []
        
        if len(all_window_sections) == 1:
            return all_window_sections[0]
        
        merged_sections = []
        merged_sections.extend(all_window_sections[0][:-1])  # All except last section
        
        for i in range(len(all_window_sections) - 1):
            current_sections = all_window_sections[i]
            next_sections = all_window_sections[i + 1]
            
            if not current_sections or not next_sections:
                continue
            
            # Merge last section of current with first section of next
            last_section = current_sections[-1]
            first_section = next_sections[0]
            
            merged_title = f"{last_section.title} / {first_section.title}"
            merged_section = DocumentSection(
                title=merged_title,
                start_index=last_section.start_index
            )
            merged_sections.append(merged_section)
            
            # Add remaining sections from next window
            if len(next_sections) > 1:
                merged_sections.extend(next_sections[1:])
        
        return merged_sections
    
    def get_sections_text(self, final_sections: List[DocumentSection], document_lines: List[Line]) -> List[Section]:
        """Populate section content and calculate end indices."""
        section_objects = []
        doc_length = len(document_lines)
        
        for i, s in enumerate(final_sections):
            if i == len(final_sections) - 1:
                end_index = doc_length - 1
            else:
                end_index = min(final_sections[i+1].start_index - 1, doc_length - 1)
            
            start_index = min(s.start_index, doc_length - 1)
            end_index = min(end_index, doc_length - 1)
            
            if start_index > end_index:
                logger.warning(f"Section '{s.title}' has invalid bounds: {start_index} > {end_index}")
                continue
            
            contents = [document_lines[j].content for j in range(start_index, end_index + 1)]
            
            section_objects.append(Section(
                title=s.title,
                content="\n".join(contents),
                start=start_index,
                end=end_index
            ))
        
        return section_objects
    
    def process_document(self, document_text: str, max_characters_per_window: int = 20000, max_concurrent_requests: int = 3) -> List[Section]:
        """Main method to process a document and return sections."""
        logger.info("Starting semantic document sectioning")  
        start_time = time.perf_counter()
        
        # Convert document to lines
        document_lines = self.str_to_lines(document_text)
        
        logger.info(f"Document converted to lines: {len(document_lines)} lines")
        
        # Create windows
        windows = self.create_document_windows(document_lines, max_characters_per_window)
        
        if not windows:
            logger.warning("No windows created")
            return []
        
        # Process windows in parallel
        all_window_sections = []
        
        with ThreadPoolExecutor(max_workers=max_concurrent_requests) as executor:
            window_futures = []
            
            for window_idx, (window_start, window_end) in enumerate(windows):
                window_text = self.get_document_text_for_window(document_lines, window_start, window_end)
                future = executor.submit(self.process_window_with_retries, window_text, window_start)
                window_futures.append((window_idx, window_start, window_end, future))
            
            # Process results
            results = [None] * len(windows)
            for window_idx, window_start, window_end, future in window_futures:
                try:
                    result = future.result()
                    if result:
                        validated_sections = self.validate_and_fix_window_sections(
                            result.sections, window_start, window_end, len(document_lines)
                        )
                        results[window_idx] = validated_sections
                        logger.info(f"Window {window_idx+1}/{len(windows)} processed: {len(validated_sections)} sections")
                    else:
                        # Fallback section
                        results[window_idx] = [DocumentSection(
                            title=f"Window {window_start}-{window_end}",
                            start_index=window_start
                        )]
                except Exception as e:
                    logger.error(f"Error processing window {window_idx+1}: {e}")
                    results[window_idx] = [DocumentSection(
                        title=f"Window {window_start}-{window_end} (Error)",
                        start_index=window_start
                    )]
            
            all_window_sections = [r for r in results if r is not None]
        
        # Merge sections across windows
        merged_sections = self.merge_sections_across_windows(all_window_sections)
        
        # Get final sections with content
        final_sections = self.get_sections_text(merged_sections, document_lines)
        
        total_duration = time.perf_counter() - start_time
        logger.info(f"Semantic sectioning complete: {len(final_sections)} sections in {total_duration:.2f}s")
        
        return final_sections

class UniversalWebScraper:
    """
    Generic web scraper that adapts to different site types
    Can handle static sites, SPAs, and complex JavaScript applications
    """
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
        })
        
        # Generic strategies for different site types
        self.strategies = {
            'static': ScrapingStrategy(
                name="static",
                javascript_required=False,
                content_selectors=['main', 'article', '.content', '#content']
            ),
            'spa_light': ScrapingStrategy(
                name="spa_light", 
                wait_time=10,
                scroll_strategy="simple",
                javascript_required=True,
                content_selectors=['main', 'app-root', '[role="main"]', '.app-content']
            ),
            'spa_heavy': ScrapingStrategy(
                name="spa_heavy",
                wait_time=20,
                scroll_strategy="progressive", 
                javascript_required=True,
                content_selectors=[
                    'main', 'app-root', '[role="main"]', '.app-content',
                    'div[class*="content"]', 'div[class*="main"]', 'div[class*="doc"]'
                ]
            ),
            'infinite_scroll': ScrapingStrategy(
                name="infinite_scroll",
                wait_time=30,
                scroll_strategy="infinite",
                javascript_required=True,
                content_selectors=['main', '.content', '.posts', '.items']
            )
        }
    
    def detect_site_architecture(self, url: str) -> str:
        """
        Generic site architecture detection based on various signals
        """
        try:
            # Quick HTTP request to analyze initial response
            response = self.session.get(url, timeout=10)
            html = response.text.lower()
            
            # Check for SPA frameworks
            spa_indicators = [
                'react', 'angular', 'vue.js', 'app-root', 'ng-app',
                'data-reactroot', 'v-app', '__next', 'nuxt'
            ]
            
            # Check for heavy JavaScript usage
            js_heavy_indicators = [
                'document.getelementbyid', 'dom manipulation',
                'ajax', 'fetch(', 'xmlhttprequest', 'api calls'
            ]
            
            # Count script tags and their complexity
            soup = BeautifulSoup(html, 'html.parser')
            script_tags = soup.find_all('script')
            script_content_length = sum(len(script.get_text()) for script in script_tags if script.get_text())
            
            # Decision logic
            if any(indicator in html for indicator in spa_indicators):
                if script_content_length > 50000:  # Heavy JS
                    return 'spa_heavy'
                else:
                    return 'spa_light'
            elif script_content_length > 20000 or any(indicator in html for indicator in js_heavy_indicators):
                return 'spa_light'
            else:
                return 'static'
                
        except Exception as e:
            print(f"Detection failed: {e}, defaulting to spa_light")
            return 'spa_light'
    
    def scrape_with_requests(self, url: str, strategy: ScrapingStrategy) -> Optional[str]:
        """Generic requests-based scraping for static sites"""
        try:
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Remove noise
            for element in soup(['script', 'style', 'nav', 'footer', 'header', 'aside']):
                element.decompose()
            
            # Try different content selectors
            for selector in strategy.content_selectors:
                try:
                    elements = soup.select(selector)
                    for element in elements:
                        content = element.get_text(separator='\n', strip=True)
                        if len(content) > 1000:  # Quality threshold
                            return self._clean_content(content)
                except:
                    continue
            
            # Fallback to body
            body_content = soup.get_text(separator='\n', strip=True)
            return self._clean_content(body_content) if len(body_content) > 500 else None
            
        except Exception as e:
            print(f"Requests scraping failed: {e}")
            return None
    
    def scrape_with_selenium(self, url: str, strategy: ScrapingStrategy) -> Optional[str]:
        """Generic Selenium-based scraping for JavaScript-heavy sites"""
        if not SELENIUM_AVAILABLE:
            print("❌ Selenium not available for JavaScript-heavy sites")
            return None
            
        driver = None
        try:
            # Generic Chrome setup
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--disable-blink-features=AutomationControlled')
            chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
            chrome_options.add_experimental_option('useAutomationExtension', False)
            
            driver = webdriver.Chrome(options=chrome_options)
            driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            
            print(f"Loading {url} with {strategy.name} strategy...")
            driver.get(url)
            
            # Generic wait strategy
            time.sleep(strategy.wait_time)
            
            # Wait for body to be present
            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            
            # Apply scrolling strategy
            self._apply_scroll_strategy(driver, strategy.scroll_strategy)
            
            # Try to find content using strategy selectors
            for selector in strategy.content_selectors:
                try:
                    elements = driver.find_elements(By.CSS_SELECTOR, selector)
                    for element in elements:
                        content = element.text
                        if len(content) > 1000:
                            print(f"Found content with selector: {selector}")
                            return self._clean_content(content)
                except:
                    continue
            
            # Fallback to body
            body_text = driver.find_element(By.TAG_NAME, "body").text
            return self._clean_content(body_text) if len(body_text) > 500 else None
            
        except Exception as e:
            print(f"Selenium scraping failed: {e}")
            return None
        finally:
            if driver:
                driver.quit()
    
    def _apply_scroll_strategy(self, driver, scroll_strategy: str):
        """Apply different scrolling strategies based on site needs"""
        if scroll_strategy == "simple":
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            
        elif scroll_strategy == "progressive":
            # Scroll in steps to trigger lazy loading
            total_height = driver.execute_script("return document.body.scrollHeight")
            for i in range(0, total_height, total_height // 5):
                driver.execute_script(f"window.scrollTo(0, {i});")
                time.sleep(2)
            
        elif scroll_strategy == "infinite":
            # Handle infinite scroll pages
            last_height = driver.execute_script("return document.body.scrollHeight")
            attempts = 0
            max_attempts = 10
            
            while attempts < max_attempts:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(3)
                
                new_height = driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height
                attempts += 1
    
    def _clean_content(self, content: str) -> str:
        """Generic content cleaning"""
        lines = [line.strip() for line in content.split('\n') if line.strip() and len(line.strip()) > 3]
        return '\n'.join(lines)
    
    def scrape_url(self, url: str, force_strategy: Optional[str] = None) -> Optional[str]:
        """
        Main method: Generic scraping with automatic strategy detection
        """
        print(f"🌐 Starting universal scraping for: {url}")
        
        # Detect or use forced strategy
        if force_strategy and force_strategy in self.strategies:
            strategy_name = force_strategy
        else:
            strategy_name = self.detect_site_architecture(url)
        
        strategy = self.strategies[strategy_name]
        print(f"🎯 Using strategy: {strategy.name}")
        
        # Try appropriate scraping method
        if strategy.javascript_required:
            content = self.scrape_with_selenium(url, strategy)
        else:
            # Try requests first, fallback to Selenium if needed
            content = self.scrape_with_requests(url, strategy)
            if not content or len(content) < 1000:
                print("📋 Requests failed, trying Selenium...")
                content = self.scrape_with_selenium(url, strategy)
        
        if content and len(content) > 500:
            print(f"✅ Successfully scraped {len(content)} characters")
            return content
        else:
            print("❌ Failed to scrape meaningful content")
            return None


class HybridScraper(UniversalWebScraper):
    """
    Hybrid approach: Generic base with site-specific optimizations
    Best of both worlds: Universal capability + targeted efficiency
    """
    
    def __init__(self):
        super().__init__()
        
        # Site-specific optimizations
        self.site_configs = {
            'developer.dell.com': {
                'strategy': 'spa_heavy',
                'wait_time': 25,
                'custom_selectors': ['app-root', 'div[class*="content"]', '.documentation'],
                'requires_scroll': True
            },
            'hitachivantara.com': {
                'strategy': 'spa_heavy', 
                'wait_time': 15,
                'custom_selectors': ['main', '.content', '.documentation'],
                'requires_scroll': True
            },
            'developer.cisco.com': {
                'strategy': 'spa_light',
                'wait_time': 10,
                'custom_selectors': ['.content', '.api-docs', 'main'],
                'json_extraction': True
            },
            'docs.aws.amazon.com': {
                'strategy': 'static',
                'custom_selectors': ['main', '.main-content', '#main-content']
            },
            'developer.github.com': {
                'strategy': 'spa_light',
                'custom_selectors': ['.markdown-body', 'main', '.content']
            }
        }
    
    def get_site_config(self, url: str) -> Dict[str, Any]:
        """Get site-specific configuration if available"""
        domain = urlparse(url).netloc.lower()
        
        for site_domain, config in self.site_configs.items():
            if site_domain in domain:
                return config
        
        # Return generic config
        return {'strategy': None}
    
    def scrape_url(self, url: str, force_strategy: Optional[str] = None) -> Optional[str]:
        """
        Enhanced scraping with site-specific optimizations
        """
        print(f"🌐 Starting hybrid scraping for: {url}")
        
        # Check for site-specific config
        site_config = self.get_site_config(url)
        
        if site_config.get('strategy'):
            # Use site-specific optimization
            strategy_name = site_config['strategy']
            strategy = self.strategies[strategy_name]
            
            # Apply site-specific modifications
            if 'wait_time' in site_config:
                strategy.wait_time = site_config['wait_time']
            if 'custom_selectors' in site_config:
                strategy.content_selectors = site_config['custom_selectors']
            
            print(f"🎯 Using optimized strategy for this site: {strategy_name}")
        else:
            # Fall back to generic detection
            strategy_name = force_strategy or self.detect_site_architecture(url)
            strategy = self.strategies[strategy_name]
            print(f"🎯 Using generic strategy: {strategy_name}")
        
        # Execute scraping
        if strategy.javascript_required:
            content = self.scrape_with_selenium(url, strategy)
        else:
            content = self.scrape_with_requests(url, strategy)
            if not content or len(content) < 1000:
                print("📋 Requests failed, trying Selenium...")
                content = self.scrape_with_selenium(url, strategy)
        
        # Site-specific post-processing
        if content and site_config.get('json_extraction'):
            content = self._extract_json_content(content)
        
        if content and len(content) > 500:
            print(f"✅ Successfully scraped {len(content)} characters")
            return content
        else:
            print("❌ Failed to scrape meaningful content")
            return None
    
    def _extract_json_content(self, html_content: str) -> str:
        """Extract JSON from HTML for sites like Cisco"""
        try:
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # Look for JSON in script tags
            script_tags = soup.find_all('script')
            for script in script_tags:
                if script.string:
                    content = script.string.strip()
                    if content.startswith('{') or content.startswith('['):
                        try:
                            json.loads(content)
                            print(f"✅ Found JSON in script tag: {len(content)} chars")
                            return content
                        except:
                            continue
            
            # Look for JSON patterns in body text
            body_text = soup.get_text()
            json_patterns = [
                r'\{[^{}]*"type"\s*:\s*"api"[^{}]*\}',
                r'\{[^{}]*"title"[^{}]*"description"[^{}]*\}',
            ]
            
            for pattern in json_patterns:
                matches = re.findall(pattern, body_text, re.DOTALL)
                for match in matches:
                    try:
                        start = body_text.find(match)
                        if start != -1:
                            brace_count = 0
                            end = start
                            for i, char in enumerate(body_text[start:], start):
                                if char == '{':
                                    brace_count += 1
                                elif char == '}':
                                    brace_count -= 1
                                    if brace_count == 0:
                                        end = i + 1
                                        break
                            
                            json_content = body_text[start:end]
                            json.loads(json_content)
                            print(f"✅ Found JSON in body: {len(json_content)} chars")
                            return json_content
                    except:
                        continue
            
            return html_content
            
        except Exception as e:
            print(f"❌ JSON extraction failed: {e}")
            return html_content 

class APIEntitiesExtractor:
    def __init__(self, openai_api_key: str):
        self.openai_api_key = openai_api_key
        
        if LANGCHAIN_AVAILABLE:
            self.llm = ChatOpenAI(
                model="gpt-4.1-mini-2025-04-14", 
                api_key=openai_api_key,
                temperature=0.1,
                max_tokens=4000,
                timeout=60,
                max_retries=3
            )
        else:
            self.llm = None
            print("Warning: LangChain not available, using OpenAI client directly")

        # ✅ Initialize the embedding model for FAISS
        self.embedding_model = OpenAIEmbeddings(
            model="text-embedding-3-large",
            openai_api_key=openai_api_key
        )

        # ✅ Placeholder for retriever to be built after sectioning
        self.retriever = None

        # Initialize the universal scraper
        self.scraper = HybridScraper()

        # Initialize the semantic sectioner
        self.sectioner = SemanticSectioner(openai_api_key, "gpt-4.1-mini-2025-04-14")            
        

    @traceable(name="identify_source_type")
    def step1_identify_source_type(self, source: str) -> str:
        """Step 1: Identify the type of source"""
        print("🔍 Step 1: Identifying source type...")
        
        if source.startswith(('http://', 'https://')):
            source_type = "url"
        elif source.endswith('.pdf'):
            source_type = "pdf"
        elif os.path.isfile(source):
            # Check file extension
            ext = Path(source).suffix.lower()
            if ext == '.pdf':
                source_type = "pdf"
            elif ext in ['.html', '.htm']:
                source_type = "html"
            elif ext in ['.txt', '.md']:
                source_type = "text"
            else:
                source_type = "unknown"
        else:
            source_type = "unknown"
        
        print(f"✅ Source type identified: {source_type}")
        return source_type
    
    @traceable(name="convert_to_markdown")
    def step2_convert_to_markdown(self, source: str, source_type: str) -> str:
        """Step 2: Convert source data to markdown using docling or web scraping"""
        print("📄 Step 2: Converting source to markdown...")
        
        if source_type == "url":
            # Use universal scraper for web content
            print("🌐 Using universal web scraper for URL...")
            content = self.scraper.scrape_url(source)
            if content:
                # Convert HTML content to markdown-like format
                markdown_content = self._html_to_markdown(content)
                print(f"✅ Converted web content to markdown ({len(markdown_content)} characters)")
                return markdown_content
            else:
                raise ValueError(f"Failed to scrape content from URL: {source}")
                
        elif source_type == "pdf":
            if not DOCLING_AVAILABLE:
                raise ImportError("Docling is required for PDF processing but not available")
            
            # Use docling for PDF conversion
            converter = DocumentConverter()
            result = converter.convert(source)
            markdown_content = result.document.export_to_markdown()
            
        elif source_type in ["text", "unknown"]:
            with open(source, 'r', encoding='utf-8') as f:
                markdown_content = f.read()
        else:
            raise ValueError(f"Unsupported source type: {source_type}")
        
        print(f"✅ Converted to markdown ({len(markdown_content)} characters)")
        return markdown_content
    
  


    @traceable(name="semantic_sectioning")
    def step2_5_semantic_sectioning(self, markdown_content: str) -> List[Section]:
        """Step 2.5: NEW - Apply semantic sectioning to the markdown content"""
        print("📑 Step 2.5: Applying semantic sectioning...")

        try:
            # Process the markdown content through semantic sectioner
            sections = self.sectioner.process_document(
                document_text=markdown_content,
                max_characters_per_window=15000,
                max_concurrent_requests=3
            )

            print(f"✅ Semantic sectioning complete: {len(sections)} sections identified")

            # 🔁 Build FAISS documents from sections
            documents = [
                Document(
                    page_content=section.content,
                    metadata={"title": section.title, "start": section.start, "end": section.end}
                )
                for section in sections
            ]

            # ✅ Build FAISS index + retriever
            self.retriever = FAISS.from_documents(documents, self.embedding_model).as_retriever()
            print("✅ FAISS retriever initialized")

            return sections

        except Exception as e:
            print(f"❌ Semantic sectioning failed: {e}")
            fallback_section = Section(
                title="Full Document Content",
                content=markdown_content,
                start=0,
                end=len(markdown_content.split('\n')) - 1
            )
            return [fallback_section]

    def _html_to_markdown(self, html_content: str) -> str:
        """Convert HTML content to markdown-like format for LLM processing"""
        try:
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # Remove script and style elements
            for element in soup(['script', 'style']):
                element.decompose()
            
            # Convert common HTML elements to markdown
            markdown_lines = []
            
            for element in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'div', 'span', 'li']):
                text = element.get_text(strip=True)
                if not text:
                    continue
                    
                tag = element.name
                if tag.startswith('h'):
                    level = int(tag[1])
                    markdown_lines.append(f"{'#' * level} {text}")
                elif tag == 'p':
                    markdown_lines.append(text)
                    markdown_lines.append("")  # Add spacing
                elif tag == 'li':
                    markdown_lines.append(f"- {text}")
                else:
                    markdown_lines.append(text)
            
            return '\n'.join(markdown_lines)
            
        except Exception as e:
            print(f"HTML to markdown conversion failed: {e}")
            return html_content
    
    @traceable(name="extract_api_endpoints")
    def step3_identify_api_endpoints(self, sections: List[Section]) -> List[APIEndpoint]:
        """Step 3: LLM call to identify API endpoints from semantic sections"""
        print("🤖 Step 3: Identifying API endpoints with LLM from semantic sections...")
        
        all_endpoints = []
        
        for idx, section in enumerate(sections):
            print(f"Processing section {idx+1}/{len(sections)}: {section.title}")

            #safe_content = section.content.replace("{", "{{").replace("}", "}}")
            prompt = """You are an expert API documentation analyst. From the provided API documentation, identify and extract ONLY explicitly documented GET method API endpoints.

Documentation Content:
{}

STRICT REQUIREMENTS:
1. Extract ONLY endpoints that are explicitly documented with the GET method
2. DO NOT infer or assume endpoints - they must be clearly stated in the documentation
3. Look for explicit API endpoint documentation with HTTP methods specified
4. Ignore configuration objects, data structures, or tables unless they contain actual API endpoint definitions

Your task:
1. Scan the documentation for explicitly documented HTTP API endpoints
2. Identify ONLY those endpoints explicitly marked as GET method
3. Verify the endpoint has a clear API path format (e.g., /api/v1/volumes, /v2/users/id)
4. Extract detailed functionality description from the documentation
5. Assign confidence level based on documentation clarity

VALIDATION CRITERIA for GET endpoints:
- Must be explicitly documented as a GET method in the text
- Must have a clear API path structure (can be full URL or path starting with /)
- Must be described as retrieving, fetching, listing, or querying data
- Must NOT be described as creating, updating, deleting, or performing actions

ENDPOINT EXTRACTION RULES:
- Extract the COMPLETE endpoint URL if provided (e.g., https://<storage_system>:8080/api/v1/volumespacedistribution)
- If only path is provided, extract the full path (e.g., /api/v1/volumespacedistribution)
- Preserve variable placeholders.
- Include port numbers and protocol if specified
- Do not modify or truncate the endpoint format

EXCLUSION RULES:
- Skip configuration objects, data models, or table definitions
- Skip endpoints not explicitly marked as GET
- Skip inferred endpoints based on resource names
- Skip endpoints described as creating, updating, or deleting resources

OUTPUT FORMAT:
If GET endpoints are found, return JSON:
[
  {{
    "method": "GET",
    "endpoint": "Complete URL or path exactly as documented",
    "description": "Exact functionality description from documentation",
    "confidence": "high|medium|low",
    "source_text": "Brief quote from documentation showing this is a GET endpoint"
  }}
]

If NO explicit GET endpoints are found in the documentation, return:
{{
  "message": "No explicit GET endpoints found in the provided documentation.",
  "endpoints": []
}}

IMPORTANT: Extract the COMPLETE endpoint exactly as documented. If the documentation shows "https://<storage_system>:8080/api/v1/volumespacedistribution", extract the entire URL including protocol, domain placeholder, port, and path. Do not truncate to just the path portion.
""".format(section.content)



            try:
                if self.llm:
                    response = self.llm.invoke(prompt)
                    content = response.content.strip()
                else:
                    # Fallback to direct OpenAI client
                    client = OpenAI(api_key=self.openai_api_key)
                    response = client.chat.completions.create(
                        model="gpt-4.1-mini-2025-04-14",
                        messages=[
                            {"role": "system", "content": "You are an expert API documentation analyst."},
                            {"role": "user", "content": prompt}
                        ],
                        max_tokens=4000,
                        temperature=0.1
                    )
                    content = response.choices[0].message.content.strip()
                
                # Extract JSON from response
                json_start = content.find('[')
                json_end = content.rfind(']') + 1
                
                if json_start != -1 and json_end != 0:
                    json_content = content[json_start:json_end]
                    try:
                        endpoints_data = json.loads(json_content)
                        
                        for ep_data in endpoints_data:
                            if isinstance(ep_data, dict) and 'endpoint' in ep_data:
                                confidence_map = {"high": 0.9, "medium": 0.6, "low": 0.3}
                                endpoint = APIEndpoint(
                                    method=ep_data.get('method', 'GET'),
                                    endpoint=ep_data.get('endpoint', ''),
                                    description=ep_data.get('description', ''),
                                    confidence_score=confidence_map.get(ep_data.get('confidence', 'low'), 0.3)
                                )
                                all_endpoints.append(endpoint)
                        
                        print(f"✅ Found {len(endpoints_data)} endpoints in section {idx+1}")
                        
                    except json.JSONDecodeError as e:
                        print(f"JSON parsing error in section {idx+1}: {e}")
                else:
                    print(f"No valid JSON found in section {idx+1}")
                        
            except Exception as e:
                print(f"Error processing section {idx+1}: {e}")
                continue
        
        # Remove duplicates based on endpoint path
        unique_endpoints = []
        seen_endpoints = set()
        
        for endpoint in all_endpoints:
            if endpoint.endpoint not in seen_endpoints:
                seen_endpoints.add(endpoint.endpoint)
                unique_endpoints.append(endpoint)
        
        print(f"✅ Total unique endpoints identified: {len(unique_endpoints)}")
        return unique_endpoints
    
    @traceable(name="extract_api_entities")
    def step4_extract_entities(self, endpoints: List[APIEndpoint], sections: List[Section]) -> List[APIEndpoint]:
        """Step 4: Entity identification for GET method APIs only using semantic sections"""
        print("📊 Step 4: Extracting entities for GET endpoints from semantic sections...")

        get_endpoints = [ep for ep in endpoints if ep.method.upper() == 'GET']
        print(f"Processing {len(get_endpoints)} GET endpoints out of {len(endpoints)} total")

        for idx, endpoint in enumerate(get_endpoints):
            print(f"Processing endpoint {idx+1}/{len(get_endpoints)}: {endpoint.endpoint}")

            relevant_sections = self._find_relevant_sections(endpoint, sections)
            entity_found = False

            for k in range(1, len(relevant_sections) + 1):
                chunk_subset = relevant_sections[:k]
                combined_content = "\n\n".join([section.content for section in chunk_subset])

                prompt = """You are an expert in API documentation analysis and entity extraction.  
    Analyze the given API endpoint and extract **all response entities** it directly returns, as described in the documentation context.  
    Your task is to identify **every documented field** in the **API response**, along with its type and meaning.

    API Endpoint: {method} {path}  
    Description: {desc}

    Documentation Context:
    {context}

    🔍 VALIDATION STEP:
    1. Confirm the documentation context refers to the same API endpoint and method.
    2. If the context does not match, return: []

    ENTITY EXTRACTION RULES:
    Extract **all documented response fields**, including:
    - Top-level JSON object members
    - Nested object properties (e.g., inside `members[]`, `adminSpace`, etc.)
    - Calculated or derived fields mentioned in tables or examples
    - Enumeration values in the response schema
    - Fields listed in examples, response tables, or schema definitions

    DO NOT FILTER or PRIORITIZE.
    Include all of the following, even if they are:
    - Optional
    - Rare
    - Derived or calculated
    - Deeply nested
    - Technical or obscure

    Look for these documentation patterns in order:
    1. "Table X: Response message body JSON object members" 
    2. "Table Y: [Object Name] property objects"
    3. "Success" or "HTTP 200" response descriptions
    4. JSON schema or example responses

    For NESTED objects:
    - Extract ALL properties from referenced property tables
    - Include nested object properties 
    - Maintain original field names and datatypes 

    ENTITY EXTRACTION RULES:
    ✅ Include ALL documented response fields:
    - Top-level response wrapper fields
    - Array element properties 
    - Nested object properties 
    - Calculated fields mentioned in tables
    - Enumeration values and their meanings

    Exclude the following:
    - Request parameters
    - Configuration settings
    - Error messages unrelated to successful responses
    - Fields mentioned only as part of other endpoints' examples

    Return entities in this JSON format:
    ```json
    [
    {{
        "name": "entity_name",
        "datatype": "data_type",
        "description": "What this entity represents in the API response"
    }}
    ]
    """.format(method=endpoint.method, path=endpoint.endpoint, desc=endpoint.description, context=combined_content)

                try:
                    if self.llm:
                        response = self.llm.invoke(prompt)
                        content = response.content.strip()
                    else:
                        client = OpenAI(api_key=self.openai_api_key)
                        response = client.chat.completions.create(
                            model="gpt-4.1-mini-2025-04-14",
                            messages=[
                                {"role": "system", "content": "You are an expert in API documentation analysis and entity extraction."},
                                {"role": "user", "content": prompt}
                            ],
                            max_tokens=4000,
                            temperature=0.1
                        )
                        content = response.choices[0].message.content.strip()

                    json_start = content.find('[')
                    json_end = content.rfind(']') + 1

                    if json_start != -1 and json_end != 0:
                        json_content = content[json_start:json_end]
                        try:
                            entities_data = json.loads(json_content)
                            if isinstance(entities_data, list) and any("name" in e for e in entities_data):
                                endpoint.entities = entities_data
                                print(f"✅ Extracted {len(entities_data)} entities for {endpoint.endpoint}")
                                entity_found = True
                                break  # ✅ Stop after valid response
                        except json.JSONDecodeError:
                            pass

                except Exception as e:
                    print(f"Error extracting entities for {endpoint.endpoint}: {e}")
                    endpoint.entities = []

            if not entity_found:
                print(f"⚠️ No valid entities found for {endpoint.endpoint}")
                endpoint.entities = []

        return endpoints

    
    def _find_relevant_sections(self, endpoint: APIEndpoint, sections: List[Section], top_k: int = 3) -> List[Section]:
        """
        Return relevant sections using FAISS + OpenAI embeddings.
        If retriever is not initialized, fall back to top-k sections.
        """
        query = f"{endpoint.method.upper()} {endpoint.endpoint}\n\n{endpoint.description}"

        if self.retriever:
            try:
                retrieved_docs = self.retriever.get_relevant_documents(query)
                retrieved_sections = []

                for doc in retrieved_docs:
                    match = next((sec for sec in sections if sec.content.strip() == doc.page_content.strip()), None)
                    if match:
                        retrieved_sections.append(match)
                    if len(retrieved_sections) >= top_k:
                        break

                if retrieved_sections:
                    print(f"✅ Retrieved {len(retrieved_sections)} semantically relevant sections")
                    return retrieved_sections

            except Exception as e:
                print(f"⚠️ FAISS retrieval failed: {e}")

        print("⚠️ Using fallback: returning first top_k sections")
        return sections[:top_k]





    
    @traceable(name="identify_kpis")
    def step5_identify_kpis(self, endpoints: List[APIEndpoint]) -> List[APIEndpoint]:
        """Step 5: KPI identification for GET method APIs only"""
        print("📈 Step 5: Identifying KPIs for GET endpoints...")
        
        get_endpoints = [ep for ep in endpoints if ep.method.upper() == 'GET']
        print(f"Processing {len(get_endpoints)} GET endpoints for KPI identification")
        
        for idx, endpoint in enumerate(get_endpoints):
            print(f"Processing endpoint {idx+1}/{len(get_endpoints)}: {endpoint.endpoint}")
            
            # Create a comprehensive prompt for KPI identification
            entities_text = json.dumps(endpoint.entities, indent=2)if endpoint.entities else "No specific entities identified"
            
            prompt = """ROLE: You are a comprehensive KPI identification expert for storage and infrastructure monitoring systems. Your goal is to identify ALL relevant KPIs that would be valuable for monitoring, alerting, and operational decision-making.

Context: 
• You receive API endpoint metadata with available entities/fields
• API Endpoint: {} {}  
• Description: {}  

Available Entities with Details:
{}

ONLY USE PROVIDED ENTITIES

Extract KPIs ONLY from the entities explicitly listed in "Available Entities"
Do NOT infer or assume additional metrics that aren't documented
Do NOT add common storage metrics unless they appear in the entity list



KPI IDENTIFICATION APPROACH

Primary KPI Categories (Extract ALL applicable):

1.Identity & Reference KPIs

Names, IDs, UUIDs (essential for tracking and correlation)
Types, models, versions (for inventory and compatibility management)


2.Operational State KPIs

Status, state, health indicators
Availability, operational readiness
Error states, degraded conditions


3.Capacity & Space KPIs

Total capacity/space metrics
Used/allocated capacity
Free/available capacity
Reserved or shared allocations
Calculate derived metrics: Usage percentages, remaining capacity ratios


4.Performance & Activity KPIs

IOPS, throughput, bandwidth metrics
Response times, latency measurements
Queue depths, active operations
Error rates, retry counts


5.Resource Counting KPIs

Total counts of managed resources
Active vs inactive resource counts
Failed, degraded, or problematic resource counts
Allocation and utilization ratios


6.Efficiency & Optimization KPIs

Compression ratios, deduplication effectiveness
Data reduction metrics
Optimization levels and efficiency scores


7.Environmental & Physical KPIs

Power consumption, temperature readings
Physical location identifiers
Hardware health indicators


8.Time-based & Trend KPIs

Creation times, last update timestamps
Age-based metrics, lifecycle indicators
Historical trend data points



ENHANCED IDENTIFICATION RULES: 

Include KPIs that are:

-Directly available from the entity list
-Calculable from available entities (e.g., used = total - free)
-Essential for monitoring even if informational (names, IDs)
-Critical for alerting (status, health, error counts)
-Important for capacity planning (space, counts, utilization)
-Valuable for troubleshooting (state, relationships, timestamps)

KPI Extraction Strategy:

Map all entities to their most likely KPI category
Identify calculation opportunities (percentages, ratios, derived values)
Include foundational identifiers (names, IDs are always KPIs)
Prioritize operational metrics (status, health, performance)


Special Instructions for Storage Systems:

Space metrics are always critical KPIs (total, used, free, shared, private)
Volume/resource counts indicate capacity and health
State/status fields are primary operational KPIs
ID fields are essential for correlation and tracking
Calculate missing metrics where possible (e.g., utilization %)

FORBIDDEN ACTIONS

Do NOT add performance metrics (IOPS, throughput, latency) unless explicitly in entity list
Do NOT add environmental metrics (power, temperature) unless explicitly available
Do NOT add historical or trend metrics unless explicitly available
Do NOT add counts or totals unless they appear in the response structure

OUTPUT REQUIREMENTS
Provide a comprehensive JSON array containing ALL identified KPIs from the available entities, including:

Direct entity mappings
Calculated/derived metrics (clearly marked)
Essential identifiers
Operational status indicators
Capacity and performance metrics

Return only the JSON array of KPI names:
["kpi1", "kpi2", "kpi3"]""".format(endpoint.method, endpoint.endpoint, endpoint.description, entities_text)

            try:
                if self.llm:
                    response = self.llm.invoke(prompt)
                    content = response.content.strip()
                else:
                    # Fallback to direct OpenAI client
                    client = OpenAI(api_key=self.openai_api_key)
                    response = client.chat.completions.create(
                        model="gpt-4.1-mini-2025-04-14",
                        messages=[
                            {"role": "system", "content": "You are an expert in API documentation analysis and KPI identification."},
                            {"role": "user", "content": prompt}
                        ],
                        max_tokens=4000,
                        temperature=0.1
                    )
                    content = response.choices[0].message.content.strip()
                
                # Extract JSON from response
                json_start = content.find('[')
                json_end = content.rfind(']') + 1
                
                if json_start != -1 and json_end != 0:
                    json_content = content[json_start:json_end]
                    try:
                        kpis_data = json.loads(json_content)
                        kpis = []
                        
                        for kpi_data in kpis_data:
                            if isinstance(kpi_data, str):
                                kpis.append(kpi_data)
                            elif isinstance(kpi_data, dict) and 'kpi_name' in kpi_data:
                                kpi_name = kpi_data.get('kpi_name', '')
                                if kpi_name:
                                    kpis.append(kpi_name)
                        
                        endpoint.kpis = kpis
                        print(f"✅ Identified {len(kpis)} KPIs for {endpoint.endpoint}")
                        
                    except json.JSONDecodeError as e:
                        print(f"JSON parsing error for KPIs: {e}")
                        endpoint.kpis = []
                else:
                    print(f"No valid JSON found for KPIs of {endpoint.endpoint}")
                    endpoint.kpis = []
                    
            except Exception as e:
                print(f"Error identifying KPIs for {endpoint.endpoint}: {e}")
                endpoint.kpis = []
        
        return endpoints
    
    @traceable(name="generate_kpi_report")
    def step6_generate_report(self, endpoints: List[APIEndpoint], sections: List[Section]) -> Tuple[List[Dict[str, Any]], str]:
        """Step 6: Generate comprehensive report with semantic sections"""
        print("📋 Step 6: Generating comprehensive report with semantic sections...")
        
        # Prepare data for JSON output
        report_data = []
        for endpoint in endpoints:
            endpoint_dict = {
                'method': endpoint.method,
                'endpoint': endpoint.endpoint,
                'description': endpoint.description,
                'entities': endpoint.entities,
                'kpis': endpoint.kpis,
                'confidence_score': endpoint.confidence_score
            }
            report_data.append(endpoint_dict)
        
        # Generate markdown report
        markdown_report = self._generate_markdown_report(endpoints, sections)
        
        print(f"✅ Generated report with {len(report_data)} endpoints")
        return report_data, markdown_report
    
    def _generate_markdown_report(self, endpoints: List[APIEndpoint], sections: List[Section]) -> str:
        """Generate a comprehensive markdown report with semantic sections"""
        report_lines = [
            "# API Endpoints Analysis Report",
            "",
            f"## Summary",
            f"- Total endpoints analyzed: {len(endpoints)}",
            f"- GET endpoints: {len([ep for ep in endpoints if ep.method.upper() == 'GET'])}",
            f"- Endpoints with entities: {len([ep for ep in endpoints if ep.entities])}",
            f"- Endpoints with KPIs: {len([ep for ep in endpoints if ep.kpis])}",
            f"- Semantic sections identified: {len(sections)}",
            "",
            "## Semantic Document Sections",
            ""
        ]
        
        # Add semantic sections overview
        for i, section in enumerate(sections, 1):
            report_lines.extend([
                f"### Section {i}: {section.title}",
                f"**Lines:** {section.start} - {section.end}",
                f"**Content Preview:** {section.content[:200]}...",
                ""
            ])
        
        report_lines.extend([
            "## Detailed Endpoint Analysis",
            ""
        ])
        
        for i, endpoint in enumerate(endpoints, 1):
            report_lines.extend([
                f"### {i}. {endpoint.method} {endpoint.endpoint}",
                f"**Description:** {endpoint.description}",
                f"**Confidence Score:** {endpoint.confidence_score:.2f}",
                ""
            ])
            
            if endpoint.entities:
                report_lines.extend([
                    "**Entities:**",
                    *[f"- {entity}" for entity in endpoint.entities],
                    ""
                ])
            
            if endpoint.kpis:
                report_lines.extend([
                    "**KPIs:**",
                    *[f"- {kpi}" for kpi in endpoint.kpis],
                    ""
                ])
            
            report_lines.append("---")
            report_lines.append("")
        
        return '\n'.join(report_lines)
    
    @traceable(name="run_full_pipeline")
    def process_document(self, source: str) -> Tuple[List[Dict[str, Any]], str]:
        """Main processing pipeline with semantic sectioning"""
        print(f"🚀 Starting enhanced API analysis pipeline for: {source}")
        
        # Step 1: Identify source type
        
        source_type = self.step1_identify_source_type(source)
        
        # Step 2: Convert to markdown
        markdown_content = self.step2_convert_to_markdown(source, source_type)
        
        # Step 2.5: NEW - Apply semantic sectioning
        sections = self.step2_5_semantic_sectioning(markdown_content)
        
        # Step 3: Identify API endpoints from semantic sections
        endpoints = self.step3_identify_api_endpoints(sections)
        
        if not endpoints:
            print("❌ No API endpoints found")
            return [], "# API Analysis Report\n\nNo API endpoints were identified in the provided content."
        
        # Step 4: Extract entities using semantic sections
        endpoints = self.step4_extract_entities(endpoints, sections)
        
        # Step 5: Identify KPIs
        endpoints = self.step5_identify_kpis(endpoints)
        
        # Step 6: Generate report with semantic sections
        report_data, markdown_report = self.step6_generate_report(endpoints, sections)
        
        print("✅ Enhanced pipeline completed successfully")
        return report_data, markdown_report 

def main():
    # Configuration
    openai_api_key = os.getenv('OPENAI_API_KEY')
    if not openai_api_key:
        print("❌ OPENAI_API_KEY environment variable not set")
        print("Please set your OpenAI API key:")
        print("export OPENAI_API_KEY='your-api-key-here'")
        return
    
    OPENAI_API_KEY = ""  # Replace with your actual OpenAI API key
    
    # Initialize LangSmith tracing
    os.environ["LANGSMITH_TRACING"] = "true"
    os.environ["LANGSMITH_API_KEY"] = ""
    os.environ["LANGSMITH_ENDPOINT"] = "https://api.smith.langchain.com"
    os.environ["LANGSMITH_PROJECT"] = "aiops-to-metrics-final"
    # Initialize extractor
    extractor = APIEntitiesExtractor(openai_api_key)
    
    # Test with different source types
    test_sources = [
        # URLs
        #"https://developer.cisco.com/meraki/api-v1/get-network-appliance-connectivity-monitoring-destinations/",
        #"https://developer.dell.com/apis/3028/versions/5.2.0/docs/TUTORIALS/tutorials.md",
        # "https://docs.hitachivantara.com/r/en-us/ops-center-administrator/10.9.x/mk-99adm002/file-storage-management-resources",
        
        # Local files (uncomment and modify paths as needed)
         #"/home/siddhi/Documents/Siddhi/25_Q1/API_to_metrics/Sample_pdfs/_HPE 3PAR Web Services API Developer's Guide-1-150.md",
        "/home/siddhi/Documents/Siddhi/25_Q1/API_to_metrics/Sample_pdfs/_HPE 3PAR Web Services API Developer's Guide.pdf"
        #"/home/siddhi/Documents/Siddhi/25_Q1/API_to_metrics/Sample_pdfs/Versa Analytics 21.1 API Reference Guide.pdf"
        #"/home/siddhi/Documents/Siddhi/25_Q1/API_to_metrics/Sample_pdfs/_HPE 3PAR Web Services API Developer's Guide-1-150.pdf"
        #"/home/siddhi/Documents/Siddhi/25_Q1/API_to_metrics/Sample_pdfs/_HPE 3PAR Web Services API Developer's Guide-1-150-98-134.pdf"
        #"/home/siddhi/Documents/Siddhi/25_Q1/API_to_metrics/Sample_pdfs/Ops Center Administrator REST API Reference Guide.pdf"
    ]
    
    for source in test_sources:
        print(f"\n{'='*80}")
        print(f"Processing: {source}")
        print(f"{'='*80}")
        
        try:
            # Process the document
            report_data, markdown_report = extractor.process_document(source)
            
            # Save results
            source_name = source.replace('://', '_').replace('/', '_').replace('.', '_')
            timestamp = int(time.time())
            
            # Save JSON data
            json_filename = f"api_analysis_results_{source_name}_{timestamp}.json"
            with open(json_filename, 'w') as f:
                json.dump(report_data, f, indent=2)
            print(f"✅ Saved JSON results to: {json_filename}")
            
            # Save markdown report
            md_filename = f"api_analysis_report_{source_name}_{timestamp}.md"
            with open(md_filename, 'w') as f:
                f.write(markdown_report)
            print(f"✅ Saved markdown report to: {md_filename}")
            
            # Save semantic sections separately
            if hasattr(extractor, 'sectioner') and hasattr(extractor.sectioner, 'last_sections'):
                sections_filename = f"semantic_sections_{source_name}_{timestamp}.json"
                sections_data = []
                for section in extractor.sectioner.last_sections:
                    sections_data.append({
                        'title': section.title,
                        'content': section.content,
                        'start': section.start,
                        'end': section.end
                    })
                with open(sections_filename, 'w') as f:
                    json.dump(sections_data, f, indent=2)
                print(f"✅ Saved semantic sections to: {sections_filename}")
            
        except Exception as e:
            print(f"❌ Error processing {source}: {e}")
            import traceback
            traceback.print_exc()
            continue


def demo_semantic_sectioning():
    """Demo function to test semantic sectioning independently"""
    print("🧪 Testing Semantic Sectioning Demo")
    
    openai_api_key = os.getenv('OPENAI_API_KEY')
    if not openai_api_key:
        print("❌ OPENAI_API_KEY environment variable not set")
        return
    
    
    try:
        # Initialize sectioner
        sectioner = SemanticSectioner(openai_api_key, "gpt-4.1-mini-2025-04-14")
        
        # Process the sample document
        sections = sectioner.process_document(
            document_text=sample_document,
            max_characters_per_window=1000,  # Small windows for demo
            max_concurrent_requests=2
        )
        
        print(f"\n{'='*60}")
        print(f"SEMANTIC SECTIONING DEMO RESULTS")
        print(f"{'='*60}")
        print(f"Total sections found: {len(sections)}")
        print(f"{'='*60}\n")
        
        for i, section in enumerate(sections, 1):
            print(f"SECTION {i}: {section.title}")
            print(f"Lines: {section.start} - {section.end}")
            print(f"Content preview: {section.content[:150]}...")
            print("-" * 60)
        
        # Save demo results
        demo_filename = f"semantic_sectioning_demo_{int(time.time())}.json"
        sections_data = []
        for section in sections:
            sections_data.append({
                'title': section.title,
                'content': section.content,
                'start': section.start,
                'end': section.end
            })
        
        with open(demo_filename, 'w') as f:
            json.dump(sections_data, f, indent=2)
        print(f"\n✅ Demo results saved to: {demo_filename}")
        
    except Exception as e:
        print(f"❌ Demo failed: {e}")
        import traceback
        traceback.print_exc()


def test_web_scraping():
    """Test function for web scraping capabilities"""
    print("🌐 Testing Web Scraping Capabilities")
    
    test_urls = [
        "https://developer.cisco.com/meraki/api-v1/get-network-appliance-connectivity-monitoring-destinations/",
        "https://httpbin.org/html",  # Simple static site for testing
    ]
    
    scraper = HybridScraper()
    
    for url in test_urls:
        print(f"\nTesting URL: {url}")
        try:
            content = scraper.scrape_url(url)
            if content:
                print(f"✅ Successfully scraped {len(content)} characters")
                print(f"Preview: {content[:200]}...")
            else:
                print("❌ Failed to scrape content")
        except Exception as e:
            print(f"❌ Error: {e}")


def create_requirements_file():
    """Create a requirements.txt file with all necessary dependencies"""
    requirements = """# Core dependencies
requests>=2.31.0
beautifulsoup4>=4.12.0
pydantic>=2.0.0
openai>=1.0.0
instructor>=1.0.0

# Web scraping
selenium>=4.15.0

# Document processing
docling>=0.1.0

# LangChain (optional)
langchain-openai>=0.1.0
langchain-community>=0.1.0
langsmith>=0.1.0

# Utilities
pathlib2>=2.3.0
"""
    
    with open('requirements.txt', 'w') as f:
        f.write(requirements)
    print("✅ Created requirements.txt file")


def create_config_file():
    """Create a configuration file template"""
    config_template = """# API Analysis Configuration

# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-4.1-mini-2025-04-14

# Semantic Sectioning Configuration
MAX_CHARACTERS_PER_WINDOW=15000
MAX_CONCURRENT_REQUESTS=3

# Web Scraping Configuration
SELENIUM_TIMEOUT=30
REQUESTS_TIMEOUT=30

# Output Configuration
SAVE_JSON_RESULTS=true
SAVE_MARKDOWN_REPORT=true
SAVE_SEMANTIC_SECTIONS=true

# Logging Configuration
LOG_LEVEL=INFO
"""
    
    with open('config.env', 'w') as f:
        f.write(config_template)
    print("✅ Created config.env template file")


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Enhanced API Documentation Analysis with Semantic Sectioning")
    parser.add_argument("--demo", action="store_true", help="Run semantic sectioning demo")
    parser.add_argument("--test-scraping", action="store_true", help="Test web scraping capabilities")
    parser.add_argument("--create-requirements", action="store_true", help="Create requirements.txt file")
    parser.add_argument("--create-config", action="store_true", help="Create configuration template")
    parser.add_argument("--source", type=str, help="Specific source to process (URL or file path)")
    
    args = parser.parse_args()
    
    if args.create_requirements:
        create_requirements_file()
        exit(0)
    
    if args.create_config:
        create_config_file()
        exit(0)
    
    if args.test_scraping:
        test_web_scraping()
        exit(0)
    
    if args.demo:
        demo_semantic_sectioning()
        exit(0)
    
    if args.source:
        # Process specific source
        openai_api_key = ""
        if not openai_api_key:
            print("❌ OPENAI_API_KEY environment variable not set")
            exit(1)
        
        extractor = APIEntitiesExtractor(openai_api_key)
        try:
            report_data, markdown_report = extractor.process_document(args.source)
            
            # Save results
            source_name = args.source.replace('://', '_').replace('/', '_').replace('.', '_')
            timestamp = int(time.time())
            
            json_filename = f"api_analysis_results_{source_name}_{timestamp}.json"
            with open(json_filename, 'w') as f:
                json.dump(report_data, f, indent=2)
            print(f"✅ Saved JSON results to: {json_filename}")
            
            md_filename = f"api_analysis_report_{source_name}_{timestamp}.md"
            with open(md_filename, 'w') as f:
                f.write(markdown_report)
            print(f"✅ Saved markdown report to: {md_filename}")
            
        except Exception as e:
            print(f"❌ Error processing {args.source}: {e}")
            import traceback
            traceback.print_exc()
            exit(1)
    else:
        # Run main function with default test sources
        main() 