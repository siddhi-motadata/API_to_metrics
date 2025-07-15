# API Endpoints Analysis Report

## Summary
- Total endpoints analyzed: 34
- GET endpoints: 34
- Endpoints with entities: 21
- Endpoints with KPIs: 20
- Semantic sections identified: 122

## Semantic Document Sections

### Section 1: Document Header and Overview of Ops Center Administrator REST API
**Lines:** 0 - 13
**Content Preview:** <!-- image -->

## Ops Center Administrator REST API Reference Guide

10.9.x

Ops Center Administrator

MK-99ADM002-17

Last updated: 2023-10-10

Generated from docs.hitachivantara.com
...

### Section 2: File Storage Management and Virtual File Server Management Resources Overview
**Lines:** 14 - 19
**Content Preview:** ## File storage management resources

This module describes the file storage management operations.

## Virtual file server management resources
...

### Section 3: Virtual File Server Management Operations and Roles
**Lines:** 20 - 33
**Content Preview:** | Request | Method | URI | Role |
|-----------------------------------------------------|----------|----------------------------------------------------------|-----------------------------------------...

### Section 4: Listing Virtual File Servers in All Storage Systems - Description and HTTP Request
**Lines:** 34 - 45
**Content Preview:** ## Listing virtual file servers in all storage systems

You can display a list of all virtual file servers getting in all storage systems.

## HTTP request syntax (URI)

GET https://ipAddress/v1/file/...

### Section 5: Response Structure and Parameters for Listing Virtual File Servers in All Storage Systems
**Lines:** 46 - 97
**Content Preview:** ## Response structure

The response body structure is shown below:

```
{ "evses": [ { "clusterNodeId": , "enabled": , "id": , "interfaceAddresses": [ { "clusterNodeId": , "evs": , "evsId": , "ip": ""...

### Section 6: Return Codes for Listing Virtual File Servers in All Storage Systems
**Lines:** 98 - 109
**Content Preview:** ## Return codes

|   Status code | HTTP name    | Description                                    |
|---------------|--------------|------------------------------------------------|
|           200 | O...

### Section 7: Example Code for Listing Virtual File Servers in All Storage Systems
**Lines:** 110 - 119
**Content Preview:** ## Example code

Request with JSON command:

```
https://129.59.181.45/v1/file/vfs JSON Response: { "evses": [ { "clusterNodeId": 2, "enabled": true, "id": 0, "interfaceAddresses": [ ... { "clusterNod...

### Section 8: Listing Virtual File Servers in a Specific Storage System - Description and HTTP Request
**Lines:** 120 - 133
**Content Preview:** ## Listing virtual file servers in a storage system

You can display all virtual file servers in a specified storage system.

## HTTP request syntax (URI)

GET https://ipAddress/v1/file/storage-system...

### Section 9: Response Structure and Parameters for Listing Virtual File Servers in a Specific Storage System
**Lines:** 134 - 167
**Content Preview:** ## Response structure

The response body structure is shown below:

You can display all virtual file servers in a specified storage system.{ "evses":

```
[ { "clusterNodeId": , "enabled": , "id": , "...

### Section 10: Return Codes for Listing Virtual File Servers in a Specific Storage System
**Lines:** 168 - 176
**Content Preview:** ## Return codes

|   Status code | HTTP name    | Description                                                            |
|---------------|--------------|---------------------------------------------...

### Section 11: Example Code for Listing Virtual File Servers in a Specific Storage System
**Lines:** 177 - 196
**Content Preview:** ## Example code

Request with JSON command:

https://172.17.64.111/v1/file/vfs

JSON Response:

{

"evses":

```
[ { "clusterNodeId": 2, "enabled": true, "id": 0, "interfaceAddresses": [ { "clusterNod...

### Section 12: Getting a Virtual File Server from a Specified Storage System - Description and HTTP Request
**Lines:** 197 - 212
**Content Preview:** ## Getting a virtual file server

You can display information about a virtual file server from a specified storage system.

## HTTP request syntax (URI)

GET https://ipAddress/v1/file/storage-systems/...

### Section 13: Response Structure and Parameters for Getting a Virtual File Server / Virtual File Server Attributes and Properties
**Lines:** 213 - 250
**Content Preview:** ## Response structure

The response body structure is shown below:

```
{ "clusterNodeId": , "enabled": , "id": , "interfaceAddresses": [ { "clusterNodeId": , "evs": , "evsId": , "ip": "", "ipv6": tru...

### Section 14: Return Codes for Virtual File Server Operations
**Lines:** 251 - 259
**Content Preview:** ## Return codes

|   Status code | HTTP name    | Description                                                            |
|---------------|--------------|---------------------------------------------...

### Section 15: Example Code and JSON Response for Virtual File Server
**Lines:** 260 - 285
**Content Preview:** ## Example code

Request with JSON command:

```
"status": "", "type": "", "uuid": ""
```

https://172.17.64.111/v1/file/storage-systems/410500/vfs/cd0f6090-4a29-11d1-90 1c-040100050000

JSON Response...

### Section 16: Creating a Virtual File Server: HTTP Request and Parameters
**Lines:** 286 - 295
**Content Preview:** ## Creating a virtual file server

You can create a virtual file server.

## HTTP request syntax (URI)

POST https://ipAddress/v1/file/storage-systems/storageSystemId/vfs

Use the ID of the storage sy...

### Section 17: Request and Response Structure for Creating a Virtual File Server
**Lines:** 296 - 349
**Content Preview:** ## Request structure

The request body structure is shown below:

```
{ "name": "", "ipAddress": "", "subnetMask": "", "port": "", "ipv6":
```

```
"storageSystemId": "", }
```

| Parameter       | Re...

### Section 18: Return Codes for Creating a Virtual File Server
**Lines:** 350 - 363
**Content Preview:** ## Return codes

| Status code | HTTP name | Description |
|---------------|---------------------|------------------------------------------------------------------------------------------------------...

### Section 19: Example Requests for Creating Virtual File Server with IPv4 and IPv6
**Lines:** 364 - 374
**Content Preview:** Example request (EVS with IPv4 address format)

```
{ "name": "New EVS", "ipAddress": "172.17.91.102", "storageSystemId": "410304", "port": "ag1", "ipv6": false }
```

```
"subnetMask": "255.255.255.1...

### Section 20: Example Response for Creating a Virtual File Server Job
**Lines:** 375 - 388
**Content Preview:** Example code

Request with JSON command:

https://172.17.64.111/v1/file/storage-systems/410500/vfs

## Example response

```
{ "jobId": "a88bd309-fe36-4d68-b3b3-342d1edf20e8", "title": { "text": "Crea...

### Section 21: Enabling a Virtual File Server: HTTP Request and Parameters
**Lines:** 389 - 400
**Content Preview:** ## Enabling a virtual file server

You can enable a virtual file server in the storage system. Use this command to bring a virtual file server online.

## HTTP request syntax (URI)

PATCH https://ipAd...

### Section 22: Request and Response Structure for Enabling a Virtual File Server
**Lines:** 401 - 446
**Content Preview:** ## Request structure

The request body structure is shown below:

```
{ "enabled":"true" }
```

| Parameter   | Required   | Type    | Description                                                      ...

### Section 23: Return Codes for Enabling a Virtual File Server / Error Codes for Virtual File Server Operations
**Lines:** 447 - 457
**Content Preview:** ## Return codes

|   Status code | HTTP name    | Description                                                                              |
|---------------|--------------|---------------------------...

### Section 24: Example Request and Response for Enabling a Virtual File Server
**Lines:** 458 - 480
**Content Preview:** ## Example request

{

"enabled":"true"

}

## Example code

Request with JSON command:

https://172.17.64.111/v1/file/storage-systems/21000/vfs/cd0f6090-4a29-11d1-901 c-040100050000

JSON Response:

...

### Section 25: Disabling a Virtual File Server: HTTP Request, Request and Response Structure, and Return Codes
**Lines:** 481 - 543
**Content Preview:** ## Disabling a virtual file server

You can disable a virtual file server. When disabling a file server a virtual file server goes offline.

## HTTP request syntax (URI)

PATCH https://ipAddress/v1/fi...

### Section 26: Example Request and Response for Disabling a Virtual File Server
**Lines:** 544 - 562
**Content Preview:** ## Example request

{ "enabled":"false" }

## Example code

Request with JSON command:

https://172.17.64.111/v1/file/storage-systems/410500/vfs/cd0f6090-4a29-11d1-90 1c-040100050000

JSON Response:

...

### Section 27: Renaming a Virtual File Server: HTTP Request, Request and Response Structure, and Return Codes
**Lines:** 563 - 633
**Content Preview:** ## Renaming a virtual file server

You can rename a virtual file server.

## HTTP request syntax (URI)

PATCH https://ipAddress/v1/file/storage-systems/storageSystemId/vfs/vfsuuId

Use the ID of the s...

### Section 28: Example Request and Response for Renaming a Virtual File Server
**Lines:** 634 - 659
**Content Preview:** ## Example request

{

"evsName":"NewEVS"

}

## Example code

Request with JSON command:

https://172.17.64.104/v1/file/storage-systems/21000/vfs/9d869ca6-4bf7-11d1-901 c-040100020009

JSON Response:...

### Section 29: Deleting a Virtual File Server: HTTP Request, Response Structure, and Return Codes / HTTP Status Codes for Authorization and Resource Access Errors
**Lines:** 660 - 717
**Content Preview:** ## Deleting a virtual file server

You can delete a virtual file server. When you delete a virtual file server, it is automatically disabled.

## HTTP request syntax (URI)

DELETE https://ipAddress/v1...

### Section 30: Example Code for Deleting a VFS with JSON Command and Response
**Lines:** 718 - 735
**Content Preview:** ## Example code

Request with JSON command:

https://172.17.64.111/v1/file/storage-systems/410500/vfs/cd0f6090-4a29-11d1-90 1c-040100050000

JSON Response:

```
{ "jobId": "df88e4bd-b6d6-435c-8ac0-dec...

### Section 31: File Pool Management Resources and API Endpoints Overview
**Lines:** 736 - 752
**Content Preview:** ## File pool management resources

| Request             | Method   | URI                                                             | Role                                                            ...

### Section 32: Listing File Pools: HTTP Request, Response Structure, and Parameters
**Lines:** 753 - 847
**Content Preview:** ## Listing file pools

You can display a list of all file pools in a storage system.

HTTP request syntax (URI)

GET https://ipAddress/v1/file/storage-systems/storageSystemId/file-pools

Use the ID of...

### Section 33: Return Codes for Listing File Pools API
**Lines:** 848 - 856
**Content Preview:** ## Return codes

|   Status code | HTTP name    | Description                                                            |
|---------------|--------------|---------------------------------------------...

### Section 34: Example Code for Listing File Pools with JSON Response
**Lines:** 857 - 874
**Content Preview:** ## Example code

Request with JSON command:

https://172.17.64.109/v1/file/storage-systems/410209/file-pools

JSON response:

{

```
"filePools": [ { "id": "6190571495709419190", "label": "FK-Pool-2",...

### Section 35: Getting a File Pool: HTTP Request, Response Structure, and Parameters
**Lines:** 875 - 920
**Content Preview:** ## Getting a file pool

You can display information about a single file pool.

## HTTP request syntax (URI)

GET https://ipAddress/v1/file/storage-systems/storageSystemId/file-pools/poolI d

Use the I...

### Section 36: Return Codes for Getting a File Pool API
**Lines:** 921 - 929
**Content Preview:** ## Return codes

|   Status code | HTTP name    | Description                                                            |
|---------------|--------------|---------------------------------------------...

### Section 37: Example Code for Getting a File Pool with JSON Response
**Lines:** 930 - 947
**Content Preview:** ## Example code

Request with JSON command:

https://172.17.64.111/v1/file/storage-systems/410500/file-pools/61905714957094 19190

JSON response:

{

"id": "6190571495709419190",

```
"label": "FK-Poo...

### Section 38: Getting a File Pool Creation Template: HTTP Request and Response Structure / Disk and RAID Configuration Parameters
**Lines:** 948 - 995
**Content Preview:** ## Getting a file pool creation template

You can get a template for creating a new file pool in the storage system.

## HTTP request syntax (URI)

GET https://ipAddress/v1/file/storage-systems/storag...

### Section 39: HTTP Return Codes for File Pool Operations
**Lines:** 996 - 1008
**Content Preview:** ## Return codes

|   Status code | HTTP name    | Description                      |
|---------------|--------------|----------------------------------|
|           401 | Unauthorized | The operation ...

### Section 40: Example Request and Response for File Pool Templates
**Lines:** 1009 - 1019
**Content Preview:** ## Example request

https://172.17.64.122/v1/file/storage-systems/410209/templates/file-pools

## Example response

```
{ "label":"", "overCommitRatio":"200", "utilizationThreshold1":70, "utilizationT...

### Section 41: Creating a File Pool from a Template: HTTP Request and Request Body Structure
**Lines:** 1020 - 1039
**Content Preview:** ## Creating a file pool from a template

You can create a file pool from a template. When creating a file pool, block pools are automatically created.

## HTTP request syntax (URI)

POST https://ipAdd...

### Section 42: Parameters for Creating a File Pool from a Template
**Lines:** 1040 - 1060
**Content Preview:** | Parameter | Required | Type | Description |
|-----------------------|------------|---------|----------------------------------------------------------------------------------------------------------...

### Section 43: Response Structure and Parameters for File Pool Creation Job
**Lines:** 1061 - 1093
**Content Preview:** ## Response structure

The response body structure is shown below:

```
{ "jobId": "", "title": { "text": "", "messageCode": "", "parameters": { } }, "user": "", "status": "", "startDate": , "endDate"...

### Section 44: HTTP Status Codes for File Pool API Requests
**Lines:** 1094 - 1112
**Content Preview:** ## HTTP status codes

| Status code | HTTP name | Description |
|---------------|-------------|---------------------------------------------------------------------------------------------------------...

### Section 45: Example Request and Response for Creating a File Pool
**Lines:** 1113 - 1135
**Content Preview:** ## Example request

https://172.17.64.122/v1/file/storage-systems/410209/templates/file-pools/6190 571495709419190

```
{ "label":"testPool", "utilizationThreshold1":70, "utilizationThreshold2":80, "t...

### Section 46: Getting a File Pool Expansion Template: HTTP Request and Response Structure
**Lines:** 1136 - 1161
**Content Preview:** ## Getting a file pool expansion template

You can get a template to expand a file pool.

Use the ID of the storage system as the storageSystemId.

## HTTP request syntax (URI)

GET https://ipAddress/...

### Section 47: Parameters in File Pool Expansion Template Response
**Lines:** 1162 - 1183
**Content Preview:** | Parameter | Type | Description |
|-----------------------|---------|----------------------------------------------------------------------------------------------------------------------------------...

### Section 48: Return Codes for File Pool Expansion Template Retrieval
**Lines:** 1184 - 1200
**Content Preview:** ## Return codes

|   Status code | HTTP name    | Description                                                            |
|---------------|--------------|---------------------------------------------...

### Section 49: Expanding a File Pool: HTTP Request Syntax and Request Structure / File Pool Template Parameters and Tier Configuration
**Lines:** 1201 - 1240
**Content Preview:** ## Expanding a file pool

You can expand a file pool using one or more parameters.

## HTTP request syntax (URI)

PATCH https://ipAddress/v1/file/storage-systems/storageSystemId/templates/file -pool/p...

### Section 50: Response Structure for File Pool Operations
**Lines:** 1241 - 1268
**Content Preview:** ## Response structure

The response body structure is shown below:

```
{ "jobId": "", "title": { "text": "", "messageCode": "", "parameters": { } }, "user": "", "status": "", "startDate": , "endDate"...

### Section 51: HTTP Status Codes for File Pool API Requests
**Lines:** 1269 - 1287
**Content Preview:** ## HTTP status codes

|   Status code | HTTP name   | Description                                                                                         |
|---------------|-------------|-------------...

### Section 52: Example Request and Response for Creating a File Pool
**Lines:** 1288 - 1309
**Content Preview:** ## Example request

```
{ "label":"sample", "utilizationThreshold1":70, "utilizationThreshold2":80, "templateTiers":[ { "name":"Gold", "diskType":"SAS", "speed":15000, "capacity":"302195408896", "raid...

### Section 53: Modifying a File Pool: Request Syntax and Parameters
**Lines:** 1310 - 1350
**Content Preview:** ## Modifying a file pool

You can modify a file pool label.

## HTTP request syntax (URI)

POST https://ipAddress/v1/file/storage-systems/storageSystemId/templates/filepools/poolId

Use the ID of the ...

### Section 54: Response Structure and Return Codes for Modifying a File Pool / Example request for modifying a file pool with JSON payload and response
**Lines:** 1351 - 1419
**Content Preview:** ## Response structure

The response body structure is shown below:

{

"jobId": "",

```
"title": { "text": "", "messageCode": "", "parameters": { } }, "user": "", "status": "", "startDate": , "endDat...

### Section 55: Deleting a file pool: overview, HTTP request syntax, request and response structure, parameters, and return codes
**Lines:** 1420 - 1474
**Content Preview:** ## Deleting a file pool

You can delete a file pool. Deleting a file pool detaches created volumes, deletes the volumes, and then deletes the underlying block pool.

## HTTP request syntax (URI)

DELE...

### Section 56: Example request and response for deleting a file pool
**Lines:** 1475 - 1487
**Content Preview:** ## Example request

https://172.17.64.111/v1/file/storage-systems/410500/file-pools/61905714957094 19190

## Example response

```
{ "jobId": "723fddb1-2013-472b-a5da-938102352ee7", "title": { "text":...

### Section 57: File system management resources: request methods, URIs, and roles
**Lines:** 1488 - 1503
**Content Preview:** File system management resources

| Request | Method | URI | Role |
|------------------------------------------------|----------|-----------------------------------------------------------------------...

### Section 58: Listing file systems: overview, HTTP request syntax, request and response structure, and response parameters
**Lines:** 1504 - 1563
**Content Preview:** ## Listing file systems

You can display information about file systems in a specified storage system.

HTTP request syntax (URI)

GET https://ipAddress/v1/file/storage-systems/storageSystemId/file-sy...

### Section 59: Return codes for listing file systems / Example code demonstrating JSON command request and response for file systems
**Lines:** 1564 - 1589
**Content Preview:** ## Return codes

|   Status code | HTTP name    | Description                      |
|---------------|--------------|----------------------------------|
|           200 | OK           | Success.      ...

### Section 60: Getting a file system: HTTP request syntax, request and response structure, and parameter descriptions
**Lines:** 1590 - 1652
**Content Preview:** ## Getting a file system

You can display information about a specific file system.

HTTP request syntax (URI)

GET https://ipAddress/v1/file/storage-systems/storageSystemId/file-systems/fil eSystemId...

### Section 61: Return codes for getting a file system
**Lines:** 1653 - 1661
**Content Preview:** ## Return codes

|   Status code | HTTP name    | Description                                                            |
|---------------|--------------|---------------------------------------------...

### Section 62: Example code for getting a specific file system with JSON response
**Lines:** 1662 - 1683
**Content Preview:** ## Example code

Request with JSON command:

https://172.17.64.109/v1/file/storage-systems/410500/file-systems/55E9F6F812D9 CF310000000000000000

JSON response:

```
{ "id": "55E9F6F812D9CF31000000000...

### Section 63: Listing file systems in a file pool: HTTP request syntax, response structure, and parameter descriptions
**Lines:** 1684 - 1776
**Content Preview:** ## Listing file systems in a file pool

You can display information about all file systems in the specified file pool.

## HTTP request syntax (URI)

GET https://ipAddress/v1/file/storage-systems/stor...

### Section 64: Return codes for listing file systems in a file pool / Error Codes for File System API Requests
**Lines:** 1777 - 1785
**Content Preview:** ## Return codes

|   Status code | HTTP name    | Description                                                            |
|---------------|--------------|---------------------------------------------...

### Section 65: Example Code for File System API Request and JSON Response
**Lines:** 1786 - 1805
**Content Preview:** ## Example code

Request with JSON command:

https://172.17.64.111/v1/file/storage-systems/410500/file-pools/61905714957094 19190/file-systems

JSON response:

```
{ "fileSystems": [ "links": [ { "rel...

### Section 66: Listing File Systems for a Virtual File Server - Overview and HTTP Request Syntax
**Lines:** 1806 - 1821
**Content Preview:** ## Listing file systems for a virtual file server

In a specified storage system, you can display information about file systems that belong to a virtual file server.

## HTTP request syntax (URI)

GE...

### Section 67: Response Structure and Parameters for Listing File Systems
**Lines:** 1822 - 1866
**Content Preview:** ## Response structure

The response body structure is shown below:

```
{ "fileSystems": { "id": "", "label": "", "filePoolId": , "evsId": ,
```

```
"fileSystemCapacityDetails": { "capacity": , "free...

### Section 68: Return Codes for Listing File Systems API
**Lines:** 1867 - 1875
**Content Preview:** ## Return codes

|   Status code | HTTP name    | Description                                                            |
|---------------|--------------|---------------------------------------------...

### Section 69: Example Code for Listing File Systems API Request and JSON Response
**Lines:** 1876 - 1936
**Content Preview:** ## Example code

Request with JSON command:

https://172.17.64.109/v1/file/storage-systems/410304/vfs/0201EF861F061E7B00000 00000000000/file-systems

JSON response:

{

"fileSystems": [

{

"id": "020...

### Section 70: Creating a File System - Overview and HTTP Request Syntax
**Lines:** 1937 - 1946
**Content Preview:** ## Creating a file system

You can create a file system. After creating the file system, the API mounts and formats the new file system.

## HTTP request syntax (URI)

POST https://ipAddress/v1/file/s...

### Section 71: Request Structure and Parameters for Creating a File System
**Lines:** 1947 - 1962
**Content Preview:** ## Request structure

The request body structure is shown below:

```
{ "label": "", "filePoolId": "", "capacity": , "blockSize": , "evsId": "", }
```

| Parameter   | Required   | Type    | Descripti...

### Section 72: Response Structure and Parameters for File System Creation Job
**Lines:** 1963 - 2000
**Content Preview:** ## Response structure

The response body structure is shown below:

```
{ "jobId": "", "title": { "text": "", "messageCode": "", "parameters": { } }, "user": "", "status": "", "startDate": , "endDate"...

### Section 73: Return Codes for Creating a File System API
**Lines:** 2001 - 2014
**Content Preview:** ## Return codes

| Status code | HTTP name | Description |
|---------------|---------------------|------------------------------------------------------------------------------------------------------...

### Section 74: Example Request and Response for Creating a File System / Mounting a file system using Ops Center Administrator including HTTP request syntax, request and response structures, return codes, and example requests
**Lines:** 2015 - 2123
**Content Preview:** ## Example request

https://172.17.64.122/v1/file/storage-systems/410209/file-systems

## Example request

```
{ "label":"NewFS", "filePoolId":"144578117277982905", "capacity":10737418240, "blockSize"...

### Section 75: Unmounting a file system including HTTP request syntax, request and response structures, return codes, and example requests
**Lines:** 2124 - 2226
**Content Preview:** ## Unmounting a file system

You can unmount a file system.

## HTTP request syntax (URI)

PATCH https://ipAddress/v1/file/storage-systems/storageSystemId/file-systems/f ileSystemId

Use the ID of the...

### Section 76: Updating a file system including HTTP request syntax, request and response structures, and parameters / Job Attributes and Properties
**Lines:** 2227 - 2285
**Content Preview:** ## Updating a file system

You can modify a file system with one or more parameters. You can also rename or expand a file system.

## HTTP request syntax (URI)

PATCH https://ipAddress/v1/file/storage...

### Section 77: Return Codes for Job Operations
**Lines:** 2286 - 2298
**Content Preview:** ## Return codes

|   Status code | HTTP name    | Description                                                                              |
|---------------|--------------|---------------------------...

### Section 78: Example Request and Response for Job Operations
**Lines:** 2299 - 2321
**Content Preview:** ## Example request

https://172.17.64.122/v1/file/storage-systems/410209/file-systems/02029F5C117 8864D0000000000000000

## Example request

```
{ "label":"NewFS17", "expansionLimit":10737418240 }
```...

### Section 79: Deleting a File System: Overview and HTTP Request Syntax
**Lines:** 2322 - 2337
**Content Preview:** ## Deleting a file system

You can delete a file system. Unmount the file system before deleting it. When a file system is deleted all associated shares (Windows OS) and exports (Linux OS) are deleted...

### Section 80: Response Structure and Parameters for File System Deletion
**Lines:** 2338 - 2365
**Content Preview:** ## Response structure

The response body structure is shown below:

```
{ "jobId": "", "title": { "text": "", "messageCode": "", "parameters": { } }, "user": "", "status": "", "startDate": , "endDate"...

### Section 81: Return Codes for File System Deletion
**Lines:** 2366 - 2378
**Content Preview:** ## Return codes

|   Status code | HTTP name    | Description                                                                              |
|---------------|--------------|---------------------------...

### Section 82: Example Code for Deleting a File System
**Lines:** 2379 - 2395
**Content Preview:** ## Example code

Request with JSON command:

https://172.17.64.109:8183/v1/file/storage-systems/21000/file-systems/ebc4b9b8 -529e-11d1-9003-040100050000

JSON Response:

{

```
"jobId": "e10b1e6c-6985...

### Section 83: Share Management Resources and API Endpoints
**Lines:** 2396 - 2407
**Content Preview:** Share management resources

| Request | Method | URI | Role |
|---------------------------------|----------|------------------------------------------------------------------------------------------|-...

### Section 84: Listing Shares: Overview and HTTP Request Syntax
**Lines:** 2408 - 2421
**Content Preview:** ## Listing shares

You can display a list of shares in the specified storage system.

## HTTP request syntax (URI)

GET https://ipAddress/v1/file/storage-systems/storageSystemId/shares

Use the ID of ...

### Section 85: Response Structure and Parameters for Listing Shares / Resource URI Parameters Description
**Lines:** 2422 - 2467
**Content Preview:** ## Response structure

The response body structure is shown below:

```
{ "shares": [ { "id": "", "name": "", "fileSystemPath": "", "fileSystemId": "", "evsId": , "permissions": [ ], "accessConfigurat...

### Section 86: Return Codes for API Requests
**Lines:** 2468 - 2477
**Content Preview:** ## Return codes

|   Status code | HTTP name    | Description                                                                              |
|---------------|--------------|---------------------------...

### Section 87: Example Code for API Request and JSON Response
**Lines:** 2478 - 2497
**Content Preview:** ## Example code

Request with JSON command:

https://172.17.64.108/v1/file/storage-systems/410209/shares

JSON response:

```
{ "shares": [ { "id": "fdad1f82-74de-11d1-9000-ac60536d5065", "name": "C$"...

### Section 88: Listing Shares in a File System - Overview and HTTP Request Syntax
**Lines:** 2498 - 2513
**Content Preview:** ## Listing shares in a file system

You can display a list of shares in the specified file system.

## HTTP request syntax (URI)

GET https://ipAddress/v1/file/storage-systems/storageSystemId/file-sys...

### Section 89: Response Structure for Listing Shares
**Lines:** 2514 - 2575
**Content Preview:** ## Response structure

The response body structure is shown below:

```
{ "shares": [ { "id": "", "name": "", "fileSystemPath": "", "fileSystemId": "", "evsId": ,
```

"permissions":

[

],

"accessCo...

### Section 90: Parameters Description for Shares Resource
**Lines:** 2576 - 2606
**Content Preview:** | Parameter           | Type    | Description                                                                                                                                              |
|----------...

### Section 91: Return Codes for Shares API Requests
**Lines:** 2607 - 2616
**Content Preview:** ## Return codes

|   Status code | HTTP name    | Description                                                                              |
|---------------|--------------|---------------------------...

### Section 92: Example Code for Listing Shares in a File System
**Lines:** 2617 - 2634
**Content Preview:** ## Example code

Request with JSON command:

https://172.17.64.108/v1/file/storage-systems/410209/file-systems/020344B00E16 1D570000000000000000/shares

```
{ "shares": [ { "id": "f391dfe4-67df-11d1-9...

### Section 93: Getting a Share - Overview and HTTP Request Syntax
**Lines:** 2635 - 2653
**Content Preview:** ## Getting a share

You can display information about a share in the specified storage system.

## HTTP request syntax (URI)

GET https://ipAddress/v1/file/storage-systems/storageSystemId/file-systems...

### Section 94: Response Structure for Getting a Share
**Lines:** 2654 - 2690
**Content Preview:** 
{

```
"id": "", "label": "", "fileSystemPath": "", "fileSystemId": "", "evsId": 1, "permissions": [ { "name": "", "permissionType": { "allowFullControl": , "allowChange": , "allowRead": ,
"denyFullC...

### Section 95: Parameters Description for Getting a Share / Share Resource Parameters and Options
**Lines:** 2691 - 2726
**Content Preview:** | Parameter           | Type    | Description                                                                                           |
|---------------------|---------|-----------------------------...

### Section 96: Related Resource Links for Shares
**Lines:** 2727 - 2734
**Content Preview:** | Parameter   | Type   | Description                                   |
|-------------|--------|-----------------------------------------------|
|             |        | mechanism for this share.    ...

### Section 97: Return Codes for Share Operations
**Lines:** 2735 - 2744
**Content Preview:** ## Return codes

|   Status code | HTTP name    | Description                                                                              |
|---------------|--------------|---------------------------...

### Section 98: Example Code for Retrieving Share Information
**Lines:** 2745 - 2768
**Content Preview:** ## Example code

Request with JSON command:

https://172.17.64.108/v1/file/storage-systems/410209/file-systems/020187A3A0C6 7BD40000000000000000/shares/68b47fa0-63f0-11d1-965d-040100020009

JSON respo...

### Section 99: Creating a Share: HTTP Request and Request Structure
**Lines:** 2769 - 2794
**Content Preview:** ## Creating a share

You can create a share.

HTTP request syntax (URI)

POST https://ipAddress/v1/file/storage-systems/storageSystemId/shares

Use the ID of the storage system as the storageSystemId....

### Section 100: Response Structure for Share Creation Job
**Lines:** 2795 - 2827
**Content Preview:** ## Response structure

The response body structure is shown below:

```
{ "jobId": "", "title": { "text": "", "messageCode": "", "parameters": { } }, "user": "", "status": "", "startDate": , "endDate"...

### Section 101: Return Codes for Share Creation
**Lines:** 2828 - 2845
**Content Preview:** ## Return codes

| Status code | HTTP name | Description |
|---------------|-------------|--------------------------------------------------------------------------------------------------------------...

### Section 102: Example Request and Response for Creating a Share
**Lines:** 2846 - 2863
**Content Preview:** ## Example request

```
{ "shareName":"NewShare", "fileSystemPath":"\ShareFolder", "fileSystemId":"020187A3A0C67BD40000000000000000" }
```

## Example request

https://172.17.64.122/v1/file/storage-sy...

### Section 103: Modifying a Share: HTTP Request and Request Structure / File and Folder Permission Parameters
**Lines:** 2864 - 2907
**Content Preview:** ## Modifying a share

You can change the following parameters: fileSystemPath, accessConfiguration, or permissions.

## HTTP request syntax (URI)

PATCH https://ipAddress/v1/file/storage-systems/stora...

### Section 104: Response Structure for Job Operations
**Lines:** 2908 - 2935
**Content Preview:** ## Response structure

The response body structure is shown below:

```
{ "jobId": "", "title": { "text": "", "messageCode": "", "parameters": { } }, "user": "", "status": "", "startDate": , "endDate"...

### Section 105: Return Codes for API Responses
**Lines:** 2936 - 2951
**Content Preview:** ## Return codes

|   Status code | HTTP name   | Description                                                                                                                                            ...

### Section 106: Example Request for File System Permissions
**Lines:** 2952 - 2962
**Content Preview:** ## Example request

```
{ "fileSystemPath": "\\homedir3", "accessConfiguration" : "", "permissions": [ { "groupName": "Everyone", "permissionType": { "allowFullControl": false, "allowChange": true, "a...

### Section 107: Deleting a Share: API Usage and Response
**Lines:** 2963 - 3037
**Content Preview:** ## Deleting a share

You can delete a share.

## HTTP request syntax (URI)

DELETE https://ipAddress/v1/file/storage-systems/storageSystemId/file-systems/ fileSystemId/shares/shareId

Use the ID of th...

### Section 108: Export Management Resources and API Endpoints
**Lines:** 3038 - 3052
**Content Preview:** ## Export management resources

| Request                             | Method   | URI                                                 | Role                                                           ...

### Section 109: Listing Exports in a Storage System: API Details and Response Structure / Example code and JSON response for listing exports
**Lines:** 3053 - 3181
**Content Preview:** ## Listing exports in a storage system

You can display a list of exports in the specified storage system.

## HTTP request syntax (URI)

GET https://ipAddress/v1/file/storage-systems/storageSystemId/...

### Section 110: Listing exports in a file system: HTTP request syntax, request and response structure, parameters, and return codes
**Lines:** 3182 - 3243
**Content Preview:** ## Listing exports in a file system

You can display a list of exports in the specified file system.

## HTTP request syntax (URI)

GET https://ipAddress/v1/file/storage-systems/storageSystemId/file-s...

### Section 111: Example code and JSON response for listing exports in a file system
**Lines:** 3244 - 3258
**Content Preview:** ## Example code

Request with JSON command:

https://172.17.64.108/v1/file/storage-systems/410209/file-systems/020187A3A0C6 7BD40000000000000000/exports

JSON response:

```
{ "exports": [ { "id": "93...

### Section 112: Getting an export: HTTP request syntax, request and response structure, parameters, and return codes
**Lines:** 3259 - 3314
**Content Preview:** ## Getting an export

You can get information about an export in the specified file system.

## HTTP request syntax (URI)

GET https://ipAddress/v1/file/storage-systems/storageSystemId/file-systems/fi...

### Section 113: Example code and JSON response for getting an export
**Lines:** 3315 - 3333
**Content Preview:** ## Example code

Request with JSON command:

https://172.17.64.108/v1/file/storage-systems/410209/file-systems/020187A3A0C6 7BD40000000000000000/exports/e647c72a-628c-11d1-95ff-040100020009

JSON resp...

### Section 114: Creating an export: HTTP request syntax, request and response structure, parameters, and job response details / Job Object Properties and Attributes
**Lines:** 3334 - 3395
**Content Preview:** ## Creating an export

You can create an export of a file system. An export is a shared resource in the Linux OS and is used for sharing file systems.

## HTTP request syntax (URI)

POST https://ipAdd...

### Section 115: Return Codes for Job Creation and Processing Requests
**Lines:** 3396 - 3414
**Content Preview:** ## Return codes

| Status code | HTTP name | Description |
|---------------|---------------------|------------------------------------------------------------------------------------------------------...

### Section 116: Example Request and Response for Creating an Export
**Lines:** 3415 - 3432
**Content Preview:** ## Example request

```
{ "exportName":"NewExport", "fileSystemPath":"\ExportFolder", "fileSystemId":"020187A3A0C67BD40000000000000000" }
```

## Example request

https://172.17.64.122/v1/file/storage...

### Section 117: Modifying an Export: Parameters, HTTP Request, and Response Structure
**Lines:** 3433 - 3493
**Content Preview:** ## Modifying an export

You can modify an export and change the following parameters: fileSystemPath and accessConfiguration.

## HTTP request syntax (URI)

PATCH https://ipAddress/v1/file/storage-sys...

### Section 118: Return Codes for Modifying an Export
**Lines:** 3494 - 3506
**Content Preview:** ## Return codes

|   Status code | HTTP name    | Description                                                                              |
|---------------|--------------|---------------------------...

### Section 119: Example Request and Response for Modifying an Export
**Lines:** 3507 - 3524
**Content Preview:** ## Example request

```
{ "fileSystemPath":"\ExportFolder", "accessConfiguration":"" }
```

## Example request

https://172.17.64.122/v1/file/storage-systems/410209/file-systems/020131B76DBF 4DA600000...

### Section 120: Deleting an Export: HTTP Request and Response Structure
**Lines:** 3525 - 3570
**Content Preview:** ## Deleting an export

You can delete an export.

## HTTP request syntax (URI)

DELETE https://ipAddress/v1/file/storage-systems/storageSystemId/file-systems/ fileSystemId/exports/exportId

Use the ID...

### Section 121: Return Codes for Deleting an Export
**Lines:** 3571 - 3583
**Content Preview:** ## Return codes

|   Status code | HTTP name    | Description                                                                              |
|---------------|--------------|---------------------------...

### Section 122: Example Request and Response for Deleting an Export
**Lines:** 3584 - 3594
**Content Preview:** ## Example request

https://172.17.64.122/v1/file/storage-systems/410209/file-systems/020187A3A0C6 7BD40000000000000000/exports/e647c72a-628c-11d1-95ff-040100020009

## Example response

```
{ "jobId"...

## Detailed Endpoint Analysis

### 1. GET /v1/file/vfs
**Description:** Listing virtual file servers in all storage systems
**Confidence Score:** 0.90

---

### 2. GET /v1/file/storage- systems/ storageSystemId /vfs
**Description:** Listing virtual file servers in a storage system
**Confidence Score:** 0.90

---

### 3. GET /v1/file/storage- systems/ storageSystemId/ vfs /vfsuuId
**Description:** Getting a virtual file server
**Confidence Score:** 0.90

---

### 4. GET https://ipAddress/v1/file/vfs
**Description:** You can display a list of all virtual file servers getting in all storage systems.
**Confidence Score:** 0.90

---

### 5. GET https://ipAddress/v1/file/storage-systems/storageSystemId/vfs
**Description:** You can display all virtual file servers in a specified storage system.
**Confidence Score:** 0.90

---

### 6. GET https://ipAddress/v1/file/storage-systems/storageSystemId/vfs/vfsuuId
**Description:** You can display information about a virtual file server from a specified storage system.
**Confidence Score:** 0.90

---

### 7. GET /v1/file/storage- systems/ storageSystemId/ file-pools
**Description:** Listing file pools
**Confidence Score:** 0.90

**Entities:**
- {'name': 'filePools', 'datatype': 'List', 'description': 'List of file pool objects in the storage system'}
- {'name': 'id', 'datatype': 'Integer', 'description': 'ID of the pool'}
- {'name': 'label', 'datatype': 'String', 'description': 'Name of the pool'}
- {'name': 'totalCapacity', 'datatype': 'String', 'description': 'Total capacity of the specified pool type in the storage system, in bytes'}
- {'name': 'freeCapacity', 'datatype': 'String', 'description': 'Capacity available, in bytes'}
- {'name': 'usedCapacity', 'datatype': 'String', 'description': 'Sum of used capacity across all pools of the specified type in the storage system, in bytes'}
- {'name': 'healthy', 'datatype': 'Boolean', 'description': 'Whether the file pool is healthy. The health of a pool is determined by the health of all its top-level virtual devices'}
- {'name': 'chunkSize', 'datatype': 'String', 'description': 'The size of the chunks the file pool is made of'}
- {'name': 'onHDP', 'datatype': 'String', 'description': 'Whether the file pool is on HDP. Default value is true since Ops Center Administrator supports file pool creation on HDP pools'}
- {'name': 'physicalCapacity', 'datatype': 'String', 'description': 'Physical capacity of the file pool, in bytes'}
- {'name': 'tierNames', 'datatype': 'List', 'description': 'Collection of tiers, such as Diamond, Platinum, Gold, Silver, and Bronze of the underlying HDP pool. Applies only to GET file pools and file pool APIs'}
- {'name': 'tiered', 'datatype': 'Boolean', 'description': 'Whether the file pool is tiered. True when there are two underlying HDP pools; False when there is only one underlying HDP pool. Applies only to GET file pools and file pool APIs'}
- {'name': 'fileSystemAutoExpansionAllowed', 'datatype': 'Boolean', 'description': 'Whether file system auto expansion is allowed'}
- {'name': 'assignedToLocalCluster', 'datatype': 'Boolean', 'description': 'Whether the file pool is assigned to a local cluster'}
- {'name': 'tiers', 'datatype': 'List', 'description': 'Collection of tier definitions'}
- {'name': 'capacity', 'datatype': 'String', 'description': 'Capacity of the tier, in bytes'}
- {'name': 'freeSpace', 'datatype': 'String', 'description': 'Free space available in the tier, in bytes'}
- {'name': 'tierNumber', 'datatype': 'String', 'description': 'Identifier number of the tier'}

---

### 8. GET /v1/file/storage- systems/ storageSystemId/ file- pools/ poolId
**Description:** Getting a file pool
**Confidence Score:** 0.90

**Entities:**
- {'name': 'id', 'datatype': 'Integer', 'description': 'ID of the pool.'}
- {'name': 'label', 'datatype': 'String', 'description': 'Name of the pool.'}
- {'name': 'totalCapacity', 'datatype': 'String', 'description': 'Total capacity of the specified pool type in the storage system, in bytes.'}
- {'name': 'freeCapacity', 'datatype': 'String', 'description': 'Capacity available, in bytes.'}
- {'name': 'usedCapacity', 'datatype': 'String', 'description': 'Sum of used capacity across all pools of the specified type in the storage system, in bytes.'}
- {'name': 'healthy', 'datatype': 'Boolean', 'description': 'Whether the file pool is healthy. The health of a pool is determined by the health of all its top-level virtual devices.'}
- {'name': 'chunkSize', 'datatype': 'String', 'description': 'The size of the chunks the file pool is made of.'}
- {'name': 'onHDP', 'datatype': 'String', 'description': 'Whether the file pool is on HDP. Default value is set to true, since Ops Center Administrator supports file pool creation on HDP pools.'}
- {'name': 'physicalCapacity', 'datatype': 'String', 'description': 'Physical capacity of the file pool, in bytes.'}
- {'name': 'tierNames', 'datatype': 'List', 'description': 'Collection of tiers, such as Diamond, Platinum, Gold, Silver, and Bronze of the underlying HDP pool. This applies only to GET file pools and file pool APIs.'}
- {'name': 'tiered', 'datatype': 'Boolean', 'description': 'Whether the file pool is tiered. True: when there are two underlying HDP pools. False: when this is only one underlying HDP pool. This applies only to GET file pools and file pool APIs.'}
- {'name': 'fileSystemAutoExpansionAllowed', 'datatype': 'Boolean', 'description': 'Whether file system auto expansion is allowed.'}
- {'name': 'assignedToLocalCluster', 'datatype': 'Boolean', 'description': 'Whether the file pool is assigned to a local cluster.'}
- {'name': 'tiers', 'datatype': 'List', 'description': 'Collection of tier definitions.'}
- {'name': 'tiers[].capacity', 'datatype': 'String', 'description': 'Capacity of the tier.'}
- {'name': 'tiers[].freeSpace', 'datatype': 'String', 'description': 'Free space available in the tier.'}
- {'name': 'tiers[].tierNumber', 'datatype': 'String', 'description': 'Number identifier of the tier.'}

**KPIs:**
- id
- label
- totalCapacity
- freeCapacity
- usedCapacity
- usedCapacityPercentage
- healthy
- chunkSize
- onHDP
- physicalCapacity
- tierNames
- tiered
- fileSystemAutoExpansionAllowed
- assignedToLocalCluster
- tiers
- tiers[].capacity
- tiers[].freeSpace
- tiers[].tierNumber

---

### 9. GET /v1/file/storage- systems/ storageSystemId/ templates/file- pools
**Description:** Getting a file pool creation template
**Confidence Score:** 0.90

**Entities:**
- {'name': 'label', 'datatype': 'String', 'description': 'Name of the file pool.'}
- {'name': 'overCommitRatio', 'datatype': 'String', 'description': 'Percentage by which a file pool capacity is overprovisioned.'}
- {'name': 'utilizationThreshold1', 'datatype': 'Integer', 'description': 'Pool utilization thresholds in percentage (Low). "0" is always displayed in Snap Pool.'}
- {'name': 'utilizationThreshold2', 'datatype': 'Integer', 'description': 'Pool utilization thresholds in percentage (High).'}
- {'name': 'filePoolTemplateItems', 'datatype': 'String', 'description': 'Collection of the file pool template items.'}
- {'name': 'tiers', 'datatype': 'List', 'description': 'Collection of tier definitions.'}
- {'name': 'name', 'datatype': 'String', 'description': 'Name of the tier.'}
- {'name': 'templateSubTiers', 'datatype': 'List', 'description': 'List of template items that form the sub tier.'}
- {'name': 'description', 'datatype': 'String', 'description': 'Tier description, for example, diskType, raidLevel, raidLayout, and speed.'}
- {'name': 'diskType', 'datatype': 'String', 'description': 'Type of disk, such as FMD DC2, FMD, SAS, SSD, SSD(RI), SSD NVMe, or SCM NVMe.'}
- {'name': 'speed', 'datatype': 'Integer', 'description': 'Speed of the disk, measured in revolutions per minute. For FMD, SSD, SSD(RI), SSD NVMe, FMD DC2, or SCM NVMe, the speed is 0.'}
- {'name': 'capacity', 'datatype': 'Long', 'description': 'Total capacity of the system drive, in bytes.'}
- {'name': 'raidLevel', 'datatype': 'String', 'description': 'RAID level. Valid values: RAID1+0, RAID5, or RAID6.'}
- {'name': 'raidLayout', 'datatype': 'String', 'description': 'RAID layout. This RAID layout should be of the specified RAID level. Valid values: For VSP G200, G/F400, G/F600, G/F800 and VSP G/F350, G/F370, G/F700, G/F900: RAID1+0: (2D+2D) RAID5: (3D+1P), (4D+1P), (6D+1P), and (7D+1P) RAID6: (6D+2P), (14D+2P), (12D+2P)'}
- {'name': 'availableSizesInBytes', 'datatype': 'Long', 'description': 'Available sizes to use for creating and updating the pool.'}

**KPIs:**
- label
- overCommitRatio
- utilizationThreshold1
- utilizationThreshold2
- name
- description
- diskType
- speed
- capacity
- raidLevel
- raidLayout
- availableSizesInBytes
- calculatedUtilizationThresholdRange

---

### 10. GET /v1/file/storage- systems/ storageSystemId/ templates/file- pools/ poolId
**Description:** Getting a file pool expansion template
**Confidence Score:** 0.90

**Entities:**
- {'name': 'label', 'datatype': 'string', 'description': 'The label or name of the file pool expansion template.'}
- {'name': 'overCommitRatio', 'datatype': 'string', 'description': 'The over-commit ratio applied to the file pool expansion template.'}
- {'name': 'utilizationThreshold1', 'datatype': 'number', 'description': 'The first utilization threshold value for triggering expansion actions.'}
- {'name': 'utilizationThreshold2', 'datatype': 'number', 'description': 'The second utilization threshold value for triggering expansion actions.'}
- {'name': 'filePoolTemplateItems', 'datatype': 'array', 'description': 'An array of file pool template item objects representing tiers and their configurations.'}
- {'name': 'filePoolTemplateItems[].tiers', 'datatype': 'array', 'description': 'An array of tier objects within each file pool template item, detailing storage tiers.'}
- {'name': 'filePoolTemplateItems[].tiers[].tierId', 'datatype': 'string', 'description': 'The unique identifier of the storage tier.'}
- {'name': 'filePoolTemplateItems[].tiers[].tierName', 'datatype': 'string', 'description': 'The name of the storage tier.'}
- {'name': 'filePoolTemplateItems[].tiers[].capacity', 'datatype': 'number', 'description': 'The capacity allocated to this tier in the file pool template.'}
- {'name': 'filePoolTemplateItems[].tiers[].priority', 'datatype': 'number', 'description': 'The priority level of the tier within the file pool template.'}

**KPIs:**
- label
- overCommitRatio
- utilizationThreshold1
- utilizationThreshold2
- filePoolTemplateItems[].tiers[].tierId
- filePoolTemplateItems[].tiers[].tierName
- filePoolTemplateItems[].tiers[].capacity
- filePoolTemplateItems[].tiers[].priority
- filePoolTemplateItems[].tiers[].capacity_utilization_percentage (calculated)

---

### 11. GET https://ipAddress/v1/file/storage-systems/storageSystemId/file-pools
**Description:** You can display a list of all file pools in a storage system.
**Confidence Score:** 0.90

**Entities:**
- {'name': 'filePools', 'datatype': 'List', 'description': 'Collection of file pool objects in the storage system'}
- {'name': 'id', 'datatype': 'Integer', 'description': 'ID of the pool'}
- {'name': 'label', 'datatype': 'String', 'description': 'Name of the pool'}
- {'name': 'totalCapacity', 'datatype': 'String', 'description': 'Total capacity of the specified pool type in the storage system, in bytes'}
- {'name': 'freeCapacity', 'datatype': 'String', 'description': 'Capacity available, in bytes'}
- {'name': 'usedCapacity', 'datatype': 'String', 'description': 'Sum of used capacity across all pools of the specified type in the storage system, in bytes'}
- {'name': 'healthy', 'datatype': 'Boolean', 'description': 'Whether the file pool is healthy. The health of a pool is determined by the health of all its top-level virtual devices'}
- {'name': 'chunkSize', 'datatype': 'String', 'description': 'The size of the chunks the file pool is made of'}
- {'name': 'onHDP', 'datatype': 'String', 'description': 'Whether the file pool is on HDP. Default value is true, since Ops Center Administrator supports file pool creation on HDP pools'}
- {'name': 'physicalCapacity', 'datatype': 'String', 'description': 'Physical capacity of the file pool, in bytes'}
- {'name': 'tierNames', 'datatype': 'List', 'description': 'Collection of tiers, such as Diamond, Platinum, Gold, Silver, and Bronze of the underlying HDP pool. Applies only to GET file pools and file pool APIs'}
- {'name': 'tiered', 'datatype': 'Boolean', 'description': 'Whether the file pool is tiered. True when there are two underlying HDP pools; False when there is only one underlying HDP pool. Applies only to GET file pools and file pool APIs'}
- {'name': 'fileSystemAutoExpansionAllowed', 'datatype': 'Boolean', 'description': 'Whether file system auto expansion is allowed'}
- {'name': 'assignedToLocalCluster', 'datatype': 'Boolean', 'description': 'Whether the file pool is assigned to a local cluster'}
- {'name': 'tiers', 'datatype': 'List', 'description': 'Collection of tier definitions'}
- {'name': 'capacity', 'datatype': 'String', 'description': 'Capacity of the tier, in bytes'}
- {'name': 'freeSpace', 'datatype': 'String', 'description': 'Free space available in the tier, in bytes'}
- {'name': 'tierNumber', 'datatype': 'String', 'description': 'Identifier number of the tier'}

**KPIs:**
- id
- label
- healthy
- totalCapacity
- freeCapacity
- usedCapacity
- physicalCapacity
- chunkSize
- onHDP
- tierNames
- tiered
- fileSystemAutoExpansionAllowed
- assignedToLocalCluster
- capacity
- freeSpace
- tierNumber
- usedCapacityPercentage (calculated)
- freeCapacityPercentage (calculated)
- usedCapacityDerived (calculated as totalCapacity - freeCapacity)

---

### 12. GET https://ipAddress/v1/file/storage-systems/storageSystemId/file-pools/poolId
**Description:** You can display information about a single file pool.
**Confidence Score:** 0.90

**Entities:**
- {'name': 'id', 'datatype': 'Integer', 'description': 'ID of the pool.'}
- {'name': 'label', 'datatype': 'String', 'description': 'Name of the pool.'}
- {'name': 'totalCapacity', 'datatype': 'String', 'description': 'Total capacity of the specified pool type in the storage system, in bytes.'}
- {'name': 'freeCapacity', 'datatype': 'String', 'description': 'Capacity available, in bytes.'}
- {'name': 'usedCapacity', 'datatype': 'String', 'description': 'Sum of used capacity across all pools of the specified type in the storage system, in bytes.'}
- {'name': 'healthy', 'datatype': 'Boolean', 'description': 'Whether the file pool is healthy. The health of a pool is determined by the health of all its top-level virtual devices.'}
- {'name': 'chunkSize', 'datatype': 'String', 'description': 'The size of the chunks the file pool is made of.'}
- {'name': 'onHDP', 'datatype': 'String', 'description': 'Whether the file pool is on HDP. Default value is set to true, since Ops Center Administrator supports file pool creation on HDP pools.'}
- {'name': 'physicalCapacity', 'datatype': 'String', 'description': 'Physical capacity of the file pool, in bytes.'}
- {'name': 'tierNames', 'datatype': 'List', 'description': 'Collection of tiers, such as Diamond, Platinum, Gold, Silver, and Bronze of the underlying HDP pool. This applies only to GET file pools and file pool APIs.'}
- {'name': 'tiered', 'datatype': 'Boolean', 'description': 'Whether the file pool is tiered. True: when there are two underlying HDP pools. False: when this is only one underlying HDP pool. This applies only to GET file pools and file pool APIs.'}
- {'name': 'fileSystemAutoExpansionAllowed', 'datatype': 'Boolean', 'description': 'Whether file system auto expansion is allowed.'}
- {'name': 'assignedToLocalCluster', 'datatype': 'Boolean', 'description': 'Whether the file pool is assigned to a local cluster.'}
- {'name': 'tiers', 'datatype': 'List', 'description': 'Collection of tier definitions.'}
- {'name': 'tiers.capacity', 'datatype': 'String', 'description': 'Capacity of the tier.'}
- {'name': 'tiers.freeSpace', 'datatype': 'String', 'description': 'Free space available in the tier.'}
- {'name': 'tiers.tierNumber', 'datatype': 'String', 'description': 'Number identifier of the tier.'}

**KPIs:**
- id
- label
- healthy
- totalCapacity
- freeCapacity
- usedCapacity
- physicalCapacity
- chunkSize
- onHDP
- tierNames
- tiered
- fileSystemAutoExpansionAllowed
- assignedToLocalCluster
- tiers.capacity
- tiers.freeSpace
- tiers.tierNumber
- usedCapacityPercentage (calculated)
- freeCapacityPercentage (calculated)

---

### 13. GET https://ipAddress/v1/file/storage-systems/storageSystemId/templates/file-p ools
**Description:** You can get a template for creating a new file pool in the storage system.
**Confidence Score:** 0.90

**Entities:**
- {'name': 'label', 'datatype': 'String', 'description': 'Name of the file pool.'}
- {'name': 'overCommitRatio', 'datatype': 'String', 'description': 'Percentage by which a file pool capacity is overprovisioned.'}
- {'name': 'utilizationThreshold1', 'datatype': 'Integer', 'description': 'Pool utilization thresholds in percentage (Low). "0" is always displayed in Snap Pool.'}
- {'name': 'utilizationThreshold2', 'datatype': 'Integer', 'description': 'Pool utilization thresholds in percentage (High).'}
- {'name': 'filePoolTemplateItems', 'datatype': 'List', 'description': 'Collection of the file pool template items.'}
- {'name': 'tiers', 'datatype': 'List', 'description': 'Collection of tier definitions.'}
- {'name': 'name', 'datatype': 'String', 'description': 'Name of the tier.'}
- {'name': 'templateSubTiers', 'datatype': 'List', 'description': 'List of template items that form the sub tier.'}
- {'name': 'description', 'datatype': 'String', 'description': 'Tier description, for example, diskType, raidLevel, raidLayout, and speed.'}
- {'name': 'diskType', 'datatype': 'String', 'description': 'Type of disk, such as FMD DC2, FMD, SAS, SSD, SSD(RI), SSD NVMe, or SCM NVMe.'}
- {'name': 'speed', 'datatype': 'Integer', 'description': 'Speed of the disk, measured in revolutions per minute. For FMD, SSD, SSD(RI), SSD NVMe, FMD DC2, or SCM NVMe, the speed is 0.'}
- {'name': 'capacity', 'datatype': 'Long', 'description': 'Total capacity of the system drive, in bytes.'}
- {'name': 'raidLevel', 'datatype': 'String', 'description': 'RAID level. Valid values: RAID1+0, RAID5, or RAID6.'}
- {'name': 'raidLayout', 'datatype': 'String', 'description': 'RAID layout. This RAID layout should be of the specified RAID level. Valid values: For VSP G200, G/F400, G/F600, G/F800 and VSP G/F350, G/F370, G/F700, G/F900: RAID1+0: (2D+2D) RAID5: (3D+1P), (4D+1P), (6D+1P), and (7D+1P) RAID6: (6D+2P), (14D+2P), (12D+2P)'}
- {'name': 'availableSizesInBytes', 'datatype': 'List of Long', 'description': 'Available sizes to use for creating and updating the pool.'}

**KPIs:**
- label
- overCommitRatio
- utilizationThreshold1
- utilizationThreshold2
- name
- description
- diskType
- speed
- capacity
- raidLevel
- raidLayout
- availableSizesInBytes
- calculatedUtilizationThresholdRange
- calculatedOverProvisionedCapacity

---

### 14. GET https://ipAddress/v1/file/storage-systems/storageSystemId/templates/file-p ools/poolId
**Description:** You can get a template to expand a file pool.
**Confidence Score:** 0.90

**Entities:**
- {'name': 'label', 'datatype': 'string', 'description': 'The label or name of the file pool expansion template.'}
- {'name': 'overCommitRatio', 'datatype': 'string', 'description': 'The over-commit ratio allowed for the file pool expansion.'}
- {'name': 'utilizationThreshold1', 'datatype': 'number', 'description': 'The first utilization threshold value for the file pool expansion template.'}
- {'name': 'utilizationThreshold2', 'datatype': 'number', 'description': 'The second utilization threshold value for the file pool expansion template.'}
- {'name': 'filePoolTemplateItems', 'datatype': 'array', 'description': 'An array of file pool template item objects representing tiers and their configurations.'}
- {'name': 'filePoolTemplateItems[].tiers', 'datatype': 'array', 'description': 'An array of tier objects within each file pool template item, describing storage tiers.'}

**KPIs:**
- label
- overCommitRatio
- utilizationThreshold1
- utilizationThreshold2

---

### 15. GET /v1/file/storage- systems/ storageSystemId /file-systems
**Description:** Listing file systems
**Confidence Score:** 0.90

**Entities:**
- {'name': 'fileSystems', 'datatype': 'List', 'description': 'List of file system objects belonging to the specified storage system'}
- {'name': 'links', 'datatype': 'List', 'description': 'Displays related resources for the file system'}
- {'name': 'rel', 'datatype': 'String', 'description': 'Relationship type of the link (e.g., _self, _filePool1, _fsServer1)'}
- {'name': 'href', 'datatype': 'String', 'description': 'URI of the related resource'}
- {'name': 'id', 'datatype': 'Integer', 'description': 'ID of the file system'}
- {'name': 'label', 'datatype': 'String', 'description': 'Name of the file system'}
- {'name': 'filePoolId', 'datatype': 'String', 'description': 'ID of the storage pool associated with the file system'}
- {'name': 'evsId', 'datatype': 'Integer', 'description': 'ID of the virtual file server'}
- {'name': 'fileSystemCapacityDetails', 'datatype': 'Object', 'description': "Details about the file system's capacity"}
- {'name': 'capacity', 'datatype': 'String', 'description': 'The file system size limit in bytes (Min = 1, Max = 1099511627776)'}
- {'name': 'freeCapacity', 'datatype': 'String', 'description': 'Capacity available in bytes'}
- {'name': 'usedCapacity', 'datatype': 'String', 'description': 'Sum of used capacity across all pools of the specified type in the storage system, in bytes'}
- {'name': 'expansionLimit', 'datatype': 'String', 'description': 'Size of the expansion limit in bytes'}
- {'name': 'unlimitedExpansion', 'datatype': 'Boolean', 'description': 'Indicates whether the expansion is unlimited (true) or limited (false)'}
- {'name': 'status', 'datatype': 'String', 'description': "Status of the virtual file server; valid values are 'mounted' or 'unmounted'"}
- {'name': 'blockSize', 'datatype': 'String', 'description': "Block size of the file system, either '32 KiB' or '4 KiB'"}
- {'name': 'fileSystemTraits', 'datatype': 'Object', 'description': 'Characteristics of the file system describing various traits and capabilities'}
- {'name': 'readOnly', 'datatype': 'Boolean', 'description': 'Indicates whether the file system is read-only'}
- {'name': 'sysLocked', 'datatype': 'Boolean', 'description': 'Indicates whether the file system is locked'}
- {'name': 'worm', 'datatype': 'Boolean', 'description': 'Indicates if the file system is a WORM (Write Once Read Many) type'}
- {'name': 'nonStrictWorm', 'datatype': 'Boolean', 'description': 'Indicates if the file system is a non-strict WORM type used for testing before committing to strict WORM'}
- {'name': 'readCache', 'datatype': 'Boolean', 'description': 'Indicates whether the cache is read-enabled'}
- {'name': 'objectReplicationTarget', 'datatype': 'Boolean', 'description': 'Indicates whether there is an object replication target set on the file system'}
- {'name': 'ndmRecoveryTarget', 'datatype': 'Boolean', 'description': 'Indicates whether there is an object recovery target set on the file system'}
- {'name': 'dedupeSupported', 'datatype': 'Boolean', 'description': 'Indicates whether deduplication is supported on the file system'}
- {'name': 'dedupeEnabled', 'datatype': 'Boolean', 'description': 'Indicates whether deduplication is enabled on the file system'}

**KPIs:**
- id
- label
- filePoolId
- evsId
- status
- capacity
- freeCapacity
- usedCapacity
- expansionLimit
- unlimitedExpansion
- blockSize
- readOnly
- sysLocked
- worm
- nonStrictWorm
- readCache
- objectReplicationTarget
- ndmRecoveryTarget
- dedupeSupported
- dedupeEnabled
- usedCapacityPercentage (calculated)
- freeCapacityPercentage (calculated)
- remainingCapacity (calculated)

---

### 16. GET /v1/file/storage- systems/ storageSystemId /file- systems/ fileSystemId
**Description:** Getting a file system
**Confidence Score:** 0.90

**Entities:**
- {'name': 'id', 'datatype': 'Integer', 'description': 'ID of the file system.'}
- {'name': 'label', 'datatype': 'String', 'description': 'Name of the file system.'}
- {'name': 'filePoolId', 'datatype': 'String', 'description': 'ID of the storage pool.'}
- {'name': 'evsId', 'datatype': 'Integer', 'description': 'ID of the virtual file server.'}
- {'name': 'status', 'datatype': 'String', 'description': 'Status of the virtual file server. Valid values: mounted or unmounted.'}
- {'name': 'blockSize', 'datatype': 'String', 'description': 'Block size of the file system, either 32 KiB or 4KiB.'}
- {'name': 'fileSystemCapacityDetails', 'datatype': 'Object', 'description': 'The file system capacity details.'}
- {'name': 'capacity', 'datatype': 'String', 'description': 'The file system size limit in bytes. Min = 1, max = 1099511627776.'}
- {'name': 'freeCapacity', 'datatype': 'String', 'description': 'Capacity available, in bytes.'}
- {'name': 'usedCapacity', 'datatype': 'String', 'description': 'Sum of used capacity across all pools of the specified type in the storage system, in bytes.'}
- {'name': 'expansionLimit', 'datatype': 'String', 'description': 'Size of the expansion limit, in bytes.'}
- {'name': 'unlimitedExpansion', 'datatype': 'Boolean', 'description': 'Whether the expansion is limited.'}
- {'name': 'fileSystemTraits', 'datatype': 'Object', 'description': 'The characteristics of the file system. It describes whether the file system is read-only, and whether object replication is set on the file system.'}
- {'name': 'readOnly', 'datatype': 'Boolean', 'description': 'Whether the cache is read.'}
- {'name': 'sysLocked', 'datatype': 'Boolean', 'description': 'Whether the file system is locked.'}
- {'name': 'worm', 'datatype': 'Boolean', 'description': 'The file system WORM type. The server supports two types of WORM file systems: strict and non-strict.'}
- {'name': 'nonStrictWorm', 'datatype': 'Boolean', 'description': 'The nonStrictWorm file system enables users to test WORM storage before committing to a "strict" file system.'}
- {'name': 'readCache', 'datatype': 'Boolean', 'description': 'Whether the cache is read.'}
- {'name': 'objectReplicationTarget', 'datatype': 'Boolean', 'description': 'Whether there is an object replication target.'}
- {'name': 'ndmRecoveryTarget', 'datatype': 'Boolean', 'description': 'Whether there is an object recovery target.'}
- {'name': 'dedupeSupported', 'datatype': 'Boolean', 'description': 'Whether deduplication is supported.'}
- {'name': 'dedupeEnabled', 'datatype': 'Boolean', 'description': 'Whether deduplication is enabled.'}

**KPIs:**
- id
- label
- filePoolId
- evsId
- status
- blockSize
- capacity
- freeCapacity
- usedCapacity
- expansionLimit
- unlimitedExpansion
- readOnly
- sysLocked
- worm
- nonStrictWorm
- readCache
- objectReplicationTarget
- ndmRecoveryTarget
- dedupeSupported
- dedupeEnabled
- usedCapacityPercentage (calculated)
- freeCapacityPercentage (calculated)
- remainingCapacityRatio (calculated)

---

### 17. GET /v1/file/storage- systems/ storageSystemId /file- pools /poolId /file-systems
**Description:** Listing file systems in a file pool
**Confidence Score:** 0.90

**Entities:**
- {'name': 'href', 'datatype': 'String', 'description': 'URI reference for the resource, includes the resource ID'}
- {'name': 'fileSystems', 'datatype': 'List', 'description': 'List of file system objects in the specified file pool'}
- {'name': 'links', 'datatype': 'List', 'description': 'Related resource links for the file system'}
- {'name': 'rel', 'datatype': 'String', 'description': 'Relationship type of the link (e.g., _self, _filePool1, _fsServer1)'}
- {'name': 'href', 'datatype': 'String', 'description': 'URI for the related resource link'}
- {'name': 'id', 'datatype': 'Integer', 'description': 'ID of the file system'}
- {'name': 'label', 'datatype': 'String', 'description': 'Name of the file system'}
- {'name': 'filePoolId', 'datatype': 'String', 'description': 'ID of the storage pool to which the file system belongs'}
- {'name': 'evsId', 'datatype': 'Integer', 'description': 'ID of the virtual file server associated with the file system'}
- {'name': 'fileSystemCapacityDetails', 'datatype': 'Object', 'description': "Details about the file system's capacity"}
- {'name': 'capacity', 'datatype': 'String', 'description': 'The file system size limit in bytes (Min = 1, Max = 1099511627776)'}
- {'name': 'freeCapacity', 'datatype': 'String', 'description': 'Available capacity in bytes'}
- {'name': 'usedCapacity', 'datatype': 'String', 'description': 'Sum of used capacity across all pools of the specified type in the storage system, in bytes'}
- {'name': 'expansionLimit', 'datatype': 'String', 'description': 'Size of the expansion limit in bytes'}
- {'name': 'unlimitedExpansion', 'datatype': 'Boolean', 'description': 'Indicates whether the expansion is unlimited (true) or limited (false)'}
- {'name': 'status', 'datatype': 'String', 'description': "Status of the virtual file server; valid values are 'mounted' or 'unmounted'"}
- {'name': 'blockSize', 'datatype': 'String', 'description': "Block size of the file system; valid values are '32KiB' or '4KiB'"}
- {'name': 'fileSystemTraits', 'datatype': 'Object', 'description': 'Characteristics and traits of the file system'}
- {'name': 'readOnly', 'datatype': 'Boolean', 'description': 'Indicates whether the file system is read-only'}
- {'name': 'sysLocked', 'datatype': 'Boolean', 'description': 'Indicates whether the file system is locked'}
- {'name': 'worm', 'datatype': 'Boolean', 'description': 'Indicates if the file system is a WORM (Write Once Read Many) type; supports strict and non-strict types'}
- {'name': 'nonStrictWorm', 'datatype': 'Boolean', 'description': 'Indicates if the file system is a non-strict WORM type used for testing before committing to strict WORM'}
- {'name': 'readCache', 'datatype': 'Boolean', 'description': 'Indicates whether the read cache is enabled'}
- {'name': 'objectReplicationTarget', 'datatype': 'Boolean', 'description': 'Indicates whether the file system is an object replication target'}
- {'name': 'ndmRecoveryTarget', 'datatype': 'Boolean', 'description': 'Indicates whether the file system is an object recovery target'}
- {'name': 'dedupeSupported', 'datatype': 'Boolean', 'description': 'Indicates whether deduplication is supported on the file system'}
- {'name': 'dedupeEnabled', 'datatype': 'Boolean', 'description': 'Indicates whether deduplication is enabled on the file system'}

**KPIs:**
- id
- label
- filePoolId
- evsId
- capacity
- freeCapacity
- usedCapacity
- expansionLimit
- unlimitedExpansion
- status
- blockSize
- readOnly
- sysLocked
- worm
- nonStrictWorm
- readCache
- objectReplicationTarget
- ndmRecoveryTarget
- dedupeSupported
- dedupeEnabled
- usedCapacityPercentage (calculated)
- freeCapacityPercentage (calculated)
- remainingCapacity (calculated)

---

### 18. GET /v1/file/storage- systems/ storageSystemId /vfs/ vfsuuId /file- systems
**Description:** Listing file systems for a virtual file server
**Confidence Score:** 0.90

---

### 19. GET https://ipAddress/v1/file/storage-systems/storageSystemId/file-systems
**Description:** You can display information about file systems in a specified storage system.
**Confidence Score:** 0.90

**Entities:**
- {'name': 'id', 'datatype': 'Integer', 'description': 'ID of the file system.'}
- {'name': 'label', 'datatype': 'String', 'description': 'Name of the file system.'}
- {'name': 'filePoolId', 'datatype': 'String', 'description': 'ID of the storage pool.'}
- {'name': 'evsId', 'datatype': 'Integer', 'description': 'ID of the virtual file server.'}
- {'name': 'fileSystemCapacityDetails', 'datatype': 'Object', 'description': 'The file system capacity details.'}
- {'name': 'capacity', 'datatype': 'String', 'description': 'The file system size limit in bytes. Min = 1, max = 1099511627776.'}
- {'name': 'freeCapacity', 'datatype': 'String', 'description': 'Capacity available, in bytes.'}
- {'name': 'usedCapacity', 'datatype': 'String', 'description': 'Sum of used capacity across all pools of the specified type in the storage system, in bytes.'}
- {'name': 'expansionLimit', 'datatype': 'String', 'description': 'Size of the expansion limit, in bytes.'}
- {'name': 'unlimitedExpansion', 'datatype': 'Boolean', 'description': 'Whether the expansion is limited.'}
- {'name': 'status', 'datatype': 'String', 'description': 'Status of the virtual file server. Valid values: mounted or unmounted.'}
- {'name': 'blockSize', 'datatype': 'String', 'description': 'Block size of the file system, either 32 KiB or 4KiB.'}
- {'name': 'fileSystemTraits', 'datatype': 'Object', 'description': 'The characteristics of the file system. It describes whether the file system is read-only, and whether object replication is set on the file system.'}
- {'name': 'readOnly', 'datatype': 'Boolean', 'description': 'Whether the cache is read.'}
- {'name': 'sysLocked', 'datatype': 'Boolean', 'description': 'Whether the file system is locked.'}
- {'name': 'worm', 'datatype': 'Boolean', 'description': 'The file system WORM type. The server supports two types of WORM file systems: strict and non-strict.'}
- {'name': 'nonStrictWorm', 'datatype': 'Boolean', 'description': 'The nonStrictWorm file system enables users to test WORM storage before committing to a "strict" file system.'}
- {'name': 'readCache', 'datatype': 'Boolean', 'description': 'Whether the cache is read.'}
- {'name': 'objectReplicationTarget', 'datatype': 'Boolean', 'description': 'Whether there is an object replication target.'}
- {'name': 'ndmRecoveryTarget', 'datatype': 'Boolean', 'description': 'Whether there is an object recovery target.'}
- {'name': 'dedupeSupported', 'datatype': 'Boolean', 'description': 'Whether deduplication is supported.'}
- {'name': 'dedupeEnabled', 'datatype': 'Boolean', 'description': 'Whether deduplication is enabled.'}

**KPIs:**
- id
- label
- filePoolId
- evsId
- capacity
- freeCapacity
- usedCapacity
- expansionLimit
- unlimitedExpansion
- status
- blockSize
- readOnly
- sysLocked
- worm
- nonStrictWorm
- readCache
- objectReplicationTarget
- ndmRecoveryTarget
- dedupeSupported
- dedupeEnabled
- usedCapacityPercentage (calculated)
- freeCapacityPercentage (calculated)
- remainingCapacityRatio (calculated)

---

### 20. GET https://ipAddress/v1/file/storage-systems/storageSystemId/file-systems/fileSystemId
**Description:** You can display information about a specific file system.
**Confidence Score:** 0.90

**Entities:**
- {'name': 'id', 'datatype': 'Integer', 'description': 'ID of the file system.'}
- {'name': 'label', 'datatype': 'String', 'description': 'Name of the file system.'}
- {'name': 'filePoolId', 'datatype': 'String', 'description': 'ID of the storage pool.'}
- {'name': 'evsId', 'datatype': 'Integer', 'description': 'ID of the virtual file server.'}
- {'name': 'status', 'datatype': 'String', 'description': 'Status of the virtual file server. Valid values: mounted or unmounted.'}
- {'name': 'blockSize', 'datatype': 'String', 'description': 'Block size of the file system, either 32 KiB or 4KiB.'}
- {'name': 'fileSystemCapacityDetails', 'datatype': 'Object', 'description': 'The file system capacity details.'}
- {'name': 'capacity', 'datatype': 'String', 'description': 'The file system size limit in bytes. Min = 1, max = 1099511627776.'}
- {'name': 'freeCapacity', 'datatype': 'String', 'description': 'Capacity available, in bytes.'}
- {'name': 'usedCapacity', 'datatype': 'String', 'description': 'Sum of used capacity across all pools of the specified type in the storage system, in bytes.'}
- {'name': 'expansionLimit', 'datatype': 'String', 'description': 'Size of the expansion limit, in bytes.'}
- {'name': 'unlimitedExpansion', 'datatype': 'Boolean', 'description': 'Whether the expansion is limited.'}
- {'name': 'fileSystemTraits', 'datatype': 'Object', 'description': 'The characteristics of the file system. It describes whether the file system is read-only, and whether object replication is set on the file system.'}
- {'name': 'readOnly', 'datatype': 'Boolean', 'description': 'Whether the cache is read.'}
- {'name': 'sysLocked', 'datatype': 'Boolean', 'description': 'Whether the file system is locked.'}
- {'name': 'worm', 'datatype': 'Boolean', 'description': 'The file system WORM type. The server supports two types of WORM file systems: strict and non-strict.'}
- {'name': 'nonStrictWorm', 'datatype': 'Boolean', 'description': 'The nonStrictWorm file system enables users to test WORM storage before committing to a "strict" file system.'}
- {'name': 'readCache', 'datatype': 'Boolean', 'description': 'Whether the cache is read.'}
- {'name': 'objectReplicationTarget', 'datatype': 'Boolean', 'description': 'Whether there is an object replication target.'}
- {'name': 'ndmRecoveryTarget', 'datatype': 'Boolean', 'description': 'Whether there is an object recovery target.'}
- {'name': 'dedupeSupported', 'datatype': 'Boolean', 'description': 'Whether deduplication is supported.'}
- {'name': 'dedupeEnabled', 'datatype': 'Boolean', 'description': 'Whether deduplication is enabled.'}

**KPIs:**
- id
- label
- filePoolId
- evsId
- status
- blockSize
- capacity
- freeCapacity
- usedCapacity
- expansionLimit
- unlimitedExpansion
- readOnly
- sysLocked
- worm
- nonStrictWorm
- readCache
- objectReplicationTarget
- ndmRecoveryTarget
- dedupeSupported
- dedupeEnabled
- usedCapacityPercentage

---

### 21. GET https://ipAddress/v1/file/storage-systems/storageSystemId/file-pools/poolId/file-systems
**Description:** You can display information about all file systems in the specified file pool.
**Confidence Score:** 0.90

**Entities:**
- {'name': 'href', 'datatype': 'String', 'description': 'URI reference for the resource, includes the resource ID'}
- {'name': 'fileSystems', 'datatype': 'List', 'description': 'List of file system objects in the specified file pool'}
- {'name': 'links', 'datatype': 'List', 'description': 'Related resource links for the file system'}
- {'name': 'rel', 'datatype': 'String', 'description': 'Relationship type of the link (e.g., _self, _filePool1, _fsServer1)'}
- {'name': 'href', 'datatype': 'String', 'description': 'URI for the related resource link'}
- {'name': 'id', 'datatype': 'Integer', 'description': 'ID of the file system'}
- {'name': 'label', 'datatype': 'String', 'description': 'Name of the file system'}
- {'name': 'filePoolId', 'datatype': 'String', 'description': 'ID of the storage pool to which the file system belongs'}
- {'name': 'evsId', 'datatype': 'Integer', 'description': 'ID of the virtual file server associated with the file system'}
- {'name': 'fileSystemCapacityDetails', 'datatype': 'Object', 'description': "Details about the file system's capacity"}
- {'name': 'capacity', 'datatype': 'String', 'description': 'The file system size limit in bytes (minimum 1, maximum 1099511627776)'}
- {'name': 'freeCapacity', 'datatype': 'String', 'description': 'Available capacity in bytes'}
- {'name': 'usedCapacity', 'datatype': 'String', 'description': 'Sum of used capacity across all pools of the specified type in the storage system, in bytes'}
- {'name': 'expansionLimit', 'datatype': 'String', 'description': 'Size of the expansion limit in bytes'}
- {'name': 'unlimitedExpansion', 'datatype': 'Boolean', 'description': 'Indicates whether the expansion is unlimited (true) or limited (false)'}
- {'name': 'status', 'datatype': 'String', 'description': "Status of the virtual file server; valid values are 'mounted' or 'unmounted'"}
- {'name': 'blockSize', 'datatype': 'String', 'description': "Block size of the file system, either '32KiB' or '4KiB'"}
- {'name': 'fileSystemTraits', 'datatype': 'Object', 'description': 'Characteristics of the file system describing various traits and capabilities'}
- {'name': 'readOnly', 'datatype': 'Boolean', 'description': 'Indicates whether the file system is read-only'}
- {'name': 'sysLocked', 'datatype': 'Boolean', 'description': 'Indicates whether the file system is locked'}
- {'name': 'worm', 'datatype': 'Boolean', 'description': 'Indicates if the file system is a WORM (Write Once Read Many) type; supports strict and non-strict WORM'}
- {'name': 'nonStrictWorm', 'datatype': 'Boolean', 'description': 'Indicates if the file system is a non-strict WORM type used for testing before committing to strict WORM'}
- {'name': 'readCache', 'datatype': 'Boolean', 'description': 'Indicates whether the cache is read-enabled'}
- {'name': 'objectReplicationTarget', 'datatype': 'Boolean', 'description': 'Indicates whether the file system has an object replication target'}
- {'name': 'ndmRecoveryTarget', 'datatype': 'Boolean', 'description': 'Indicates whether the file system has an object recovery target'}
- {'name': 'dedupeSupported', 'datatype': 'Boolean', 'description': 'Indicates whether deduplication is supported on the file system'}
- {'name': 'dedupeEnabled', 'datatype': 'Boolean', 'description': 'Indicates whether deduplication is enabled on the file system'}

**KPIs:**
- href
- id
- label
- filePoolId
- evsId
- capacity
- freeCapacity
- usedCapacity
- expansionLimit
- unlimitedExpansion
- status
- blockSize
- readOnly
- sysLocked
- worm
- nonStrictWorm
- readCache
- objectReplicationTarget
- ndmRecoveryTarget
- dedupeSupported
- dedupeEnabled
- usedCapacityPercentage (calculated)
- freeCapacityPercentage (calculated)
- remainingCapacity (calculated)

---

### 22. GET https://ipAddress/v1/file/storage-systems/storageSystemId/vfs/vfsuuId/file -systems
**Description:** In a specified storage system, you can display information about file systems that belong to a virtual file server.
**Confidence Score:** 0.90

---

### 23. GET /v1/file/storage- systems/ storageSystemId /shares
**Description:** Listing shares
**Confidence Score:** 0.90

---

### 24. GET /v1/file/storage- systems/ storageSystemId /file- systems/ fileSystemId /shares
**Description:** Listing shares in a file system
**Confidence Score:** 0.90

**Entities:**
- {'name': 'shares', 'datatype': 'array', 'description': 'List of share objects in the specified file system'}
- {'name': 'shares[].id', 'datatype': 'string', 'description': 'Unique identifier of the share'}
- {'name': 'shares[].name', 'datatype': 'string', 'description': 'Name of the share'}
- {'name': 'shares[].path', 'datatype': 'string', 'description': 'File system path to the share'}
- {'name': 'shares[].type', 'datatype': 'string', 'description': "Type of the share, e.g., 'NFS', 'SMB'"}
- {'name': 'shares[].status', 'datatype': 'string', 'description': "Current status of the share, e.g., 'online', 'offline'"}
- {'name': 'shares[].permissions', 'datatype': 'object', 'description': 'Permissions settings associated with the share'}
- {'name': 'shares[].permissions.read', 'datatype': 'boolean', 'description': 'Indicates if read access is allowed'}
- {'name': 'shares[].permissions.write', 'datatype': 'boolean', 'description': 'Indicates if write access is allowed'}
- {'name': 'shares[].createdAt', 'datatype': 'string', 'description': 'Timestamp when the share was created (ISO 8601 format)'}
- {'name': 'shares[].owner', 'datatype': 'string', 'description': 'Owner of the share'}

**KPIs:**
- shares[].id
- shares[].name
- shares[].path
- shares[].type
- shares[].status
- shares[].permissions.read
- shares[].permissions.write
- shares[].createdAt
- shares[].owner

---

### 25. GET /v1/file/storage- systems/ storageSystemId/ file- systems/ fileSystemId/ shares/ shareId
**Description:** Getting a share
**Confidence Score:** 0.90

---

### 26. GET https://ipAddress/v1/file/storage-systems/storageSystemId/shares
**Description:** You can display a list of shares in the specified storage system.
**Confidence Score:** 0.90

---

### 27. GET https://ipAddress/v1/file/storage-systems/storageSystemId/file-systems/fileSystemId/shares
**Description:** You can display a list of shares in the specified file system.
**Confidence Score:** 0.90

---

### 28. GET https://ipAddress/v1/file/storage-systems/storageSystemId/file-systems/fileSystemId/shares/shareId
**Description:** You can display information about a share in the specified storage system.
**Confidence Score:** 0.90

---

### 29. GET /v1/file/storage- systems/ storageSystemId /exports
**Description:** Listing exports in a storage system
**Confidence Score:** 0.90

**Entities:**
- {'name': 'exports', 'datatype': 'List', 'description': 'List of export objects in the storage system'}
- {'name': 'id', 'datatype': 'Integer', 'description': 'ID of the export'}
- {'name': 'name', 'datatype': 'String', 'description': 'Name of the resource'}
- {'name': 'fileSystemPath', 'datatype': 'String', 'description': 'The file system location to be accessed through the resource. Min length = 1, max length = 80'}
- {'name': 'fileSystemId', 'datatype': 'String', 'description': 'ID of the file system. Min length = 0, max length = 256'}
- {'name': 'evsId', 'datatype': 'Integer', 'description': 'ID of the virtual file server'}
- {'name': 'accessConfiguration', 'datatype': 'String', 'description': 'The access security for this resource. Min length = 1, max length = 5957'}
- {'name': 'snapshotOptions', 'datatype': 'String', 'description': 'Snapshot access options with enumerated values: 0 = Hides and disallows access to snapshots; 1 = Hides snapshots but allows access to hidden snapshots; 3 = Displays and allows access to snapshots'}
- {'name': 'transferToReplicationTarget', 'datatype': 'String', 'description': 'NFS export transfer options with enumerated values: 0 = NFS exports are not transferred to recovered file systems; 1 = When the target file system is brought online, NFS exports are transferred; 2 = NFS exports are transferred to recovered file systems'}
- {'name': 'links', 'datatype': 'List', 'description': 'List of related resource links'}
- {'name': 'rel', 'datatype': 'String', 'description': "Relationship type of the link; possible values include '_self', '_fileSystem', '_vfs'"}
- {'name': 'href', 'datatype': 'String', 'description': 'URI that includes the resource ID or related resource identifier'}
- {'name': 'self', 'datatype': 'String', 'description': "URI that includes the resource ID (represented by link with rel='_self')"}
- {'name': 'fileSystem', 'datatype': 'String', 'description': "URI that includes the file system ID (represented by link with rel='_fileSystem')"}
- {'name': 'vfs', 'datatype': 'String', 'description': "URI that includes the virtual file server ID (represented by link with rel='_vfs')"}

**KPIs:**
- exports.id
- exports.name
- exports.fileSystemPath
- exports.fileSystemId
- exports.evsId
- exports.accessConfiguration
- exports.snapshotOptions
- exports.transferToReplicationTarget
- exports.links.rel
- exports.links.href
- exports.links.self
- exports.links.fileSystem
- exports.links.vfs

---

### 30. GET /v1/file/storage- systems/ storageSystemId /file- systems/ fileSystemId /exports
**Description:** Listing exports in a file system
**Confidence Score:** 0.90

**Entities:**
- {'name': 'exports', 'datatype': 'List', 'description': 'List of export objects in the specified file system'}
- {'name': 'id', 'datatype': 'Integer', 'description': 'ID of the export'}
- {'name': 'name', 'datatype': 'String', 'description': 'Name of the resource'}
- {'name': 'fileSystemPath', 'datatype': 'String', 'description': 'The file system location to be accessed through the resource. Min length = 1, max length = 80'}
- {'name': 'fileSystemId', 'datatype': 'String', 'description': 'ID of the file system. Min length = 0, max length = 256'}
- {'name': 'evsId', 'datatype': 'Integer', 'description': 'ID of the virtual file server'}
- {'name': 'accessConfiguration', 'datatype': 'String', 'description': 'The access security for this resource. Min length = 1, max length = 5957'}
- {'name': 'snapshotOptions', 'datatype': 'String', 'description': 'Snapshot access options with enumerated values: 0 = Hides and disallows access to snapshots; 1 = Hides snapshots but allows access to hidden snapshots; 3 = Displays and allows access to snapshots'}
- {'name': 'transferToReplicationTarget', 'datatype': 'String', 'description': 'NFS export transfer options with enumerated values: 0 = NFS exports are not transferred to recovered file systems; 1 = When the target file system is brought online, NFS exports are transferred; 2 = NFS exports are transferred to recovered file systems'}
- {'name': 'links', 'datatype': 'List', 'description': 'List of related resource link objects'}
- {'name': 'rel', 'datatype': 'String', 'description': 'Relationship type of the link (e.g., _self, _fileSystem, _vfs)'}
- {'name': 'href', 'datatype': 'String', 'description': 'URI for the related resource'}
- {'name': 'self', 'datatype': 'String', 'description': 'URI that includes the resource ID (from links with rel = _self)'}
- {'name': 'fileSystem', 'datatype': 'String', 'description': 'URI that includes the file system ID (from links with rel = _fileSystem)'}
- {'name': 'vfs', 'datatype': 'String', 'description': 'URI that includes the virtual file server ID (from links with rel = _vfs)'}

**KPIs:**
- exports.id
- exports.name
- exports.fileSystemPath
- exports.fileSystemId
- exports.evsId
- exports.accessConfiguration
- exports.snapshotOptions
- exports.transferToReplicationTarget
- exports.links.rel
- exports.links.href
- exports.links.self
- exports.links.fileSystem
- exports.links.vfs

---

### 31. GET /v1/file/storage- systems/ storageSystemId/ file- systems/ fileSystemId/ exports/ exportId
**Description:** Getting an export
**Confidence Score:** 0.90

**Entities:**
- {'name': 'id', 'datatype': 'String', 'description': 'ID of the share.'}
- {'name': 'name', 'datatype': 'String', 'description': 'Name of the resource.'}
- {'name': 'fileSystemPath', 'datatype': 'String', 'description': 'The file system location to be accessed through the resource. Min length = 1, max length = 80.'}
- {'name': 'fileSystemId', 'datatype': 'String', 'description': 'ID of the file system. Min length = 0, max length = 256.'}
- {'name': 'evsId', 'datatype': 'Integer', 'description': 'ID of the virtual file server.'}
- {'name': 'accessConfiguration', 'datatype': 'String', 'description': 'The access security for this resource. Min length = 1, max length = 5957.'}
- {'name': 'snapshotOptions', 'datatype': 'String', 'description': 'Snapshot access options: 0 = Hides and disallows access to snapshots; 1 = Hides snapshots but allows access to hidden snapshots; 3 = Displays and allows access to snapshots.'}
- {'name': 'transferToReplicationTarget', 'datatype': 'String', 'description': 'NFS export transfer options to recovered file systems: 0 = NFS exports are not transferred; 1 = When the target file system is brought online, NFS exports are transferred; 2 = NFS exports are transferred to recovered file systems.'}
- {'name': 'links', 'datatype': 'List', 'description': 'Displays related resources.'}
- {'name': 'links[].rel', 'datatype': 'String', 'description': 'Relationship type of the link (e.g., _self, _filesystem, _vfs).'}
- {'name': 'links[].href', 'datatype': 'String', 'description': 'URI for the related resource.'}
- {'name': 'self', 'datatype': 'String', 'description': 'URI that includes the resource ID.'}
- {'name': 'fileSystem', 'datatype': 'String', 'description': 'URI that includes the file system ID.'}
- {'name': 'evs', 'datatype': 'String', 'description': 'URI that includes the Virtual File Server ID.'}

**KPIs:**
- id
- name
- fileSystemPath
- fileSystemId
- evsId
- accessConfiguration
- snapshotOptions
- transferToReplicationTarget

---

### 32. GET https://ipAddress/v1/file/storage-systems/storageSystemId/exports
**Description:** You can display a list of exports in the specified storage system.
**Confidence Score:** 0.90

**Entities:**
- {'name': 'exports', 'datatype': 'Array', 'description': 'List of export objects in the specified storage system'}
- {'name': 'exports[].id', 'datatype': 'Integer', 'description': 'ID of the export'}
- {'name': 'exports[].name', 'datatype': 'String', 'description': 'Name of the resource'}
- {'name': 'exports[].fileSystemPath', 'datatype': 'String', 'description': 'The file system location to be accessed through the resource. Min length = 1, max length = 80'}
- {'name': 'exports[].fileSystemId', 'datatype': 'String', 'description': 'ID of the file system. Min length = 0, max length = 256'}
- {'name': 'exports[].evsId', 'datatype': 'Integer', 'description': 'ID of the virtual file server'}
- {'name': 'exports[].accessConfiguration', 'datatype': 'String', 'description': 'The access security for this resource. Min length = 1, max length = 5957'}
- {'name': 'exports[].snapshotOptions', 'datatype': 'String', 'description': 'Snapshot access options with enumerated values: 0 = Hides and disallows access to snapshots; 1 = Hides snapshots but allows access to hidden snapshots; 3 = Displays and allows access to snapshots'}
- {'name': 'exports[].transferToReplicationTarget', 'datatype': 'String', 'description': 'NFS export transfer options with enumerated values: 0 = NFS exports are not transferred to recovered file systems; 1 = When the target file system is brought online, NFS exports are transferred; 2 = NFS exports are transferred to recovered file systems'}
- {'name': 'exports[].links', 'datatype': 'Array', 'description': 'List of related resource links'}
- {'name': 'exports[].links[].rel', 'datatype': 'String', 'description': "Relationship type of the link; possible values include '_self', '_fileSystem', '_vfs'"}
- {'name': 'exports[].links[].href', 'datatype': 'String', 'description': 'URI for the related resource'}

**KPIs:**
- exports[].id
- exports[].name
- exports[].fileSystemPath
- exports[].fileSystemId
- exports[].evsId
- exports[].accessConfiguration
- exports[].snapshotOptions
- exports[].transferToReplicationTarget

---

### 33. GET https://ipAddress/v1/file/storage-systems/storageSystemId/file-systems/fileSystemId/exports
**Description:** You can display a list of exports in the specified file system.
**Confidence Score:** 0.90

**Entities:**
- {'name': 'exports', 'datatype': 'List', 'description': 'A list of export objects in the specified file system.'}
- {'name': 'id', 'datatype': 'Integer', 'description': 'ID of the export.'}
- {'name': 'name', 'datatype': 'String', 'description': 'Name of the resource.'}
- {'name': 'fileSystemPath', 'datatype': 'String', 'description': 'The file system location to be accessed through the resource. Minimum length = 1, maximum length = 80.'}
- {'name': 'fileSystemId', 'datatype': 'String', 'description': 'ID of the file system. Minimum length = 0, maximum length = 256.'}
- {'name': 'evsId', 'datatype': 'Integer', 'description': 'ID of the virtual file server.'}
- {'name': 'accessConfiguration', 'datatype': 'String', 'description': 'The access security configuration for this resource. Minimum length = 1, maximum length = 5957.'}
- {'name': 'snapshotOptions', 'datatype': 'String', 'description': 'Snapshot access options with enumerated values: 0 = Hides and disallows access to snapshots; 1 = Hides snapshots but allows access to hidden snapshots; 3 = Displays and allows access to snapshots.'}
- {'name': 'transferToReplicationTarget', 'datatype': 'String', 'description': 'NFS export transfer options with enumerated values: 0 = NFS exports are not transferred to recovered file systems; 1 = When the target file system is brought online, NFS exports are transferred; 2 = NFS exports are transferred to recovered file systems.'}
- {'name': 'links', 'datatype': 'List', 'description': 'List of related resource link objects.'}
- {'name': 'rel', 'datatype': 'String', 'description': "Relationship type of the link. Possible values include '_self', '_fileSystem', '_vfs'."}
- {'name': 'href', 'datatype': 'String', 'description': 'URI that corresponds to the related resource.'}
- {'name': 'self', 'datatype': 'String', 'description': "URI that includes the resource ID (from the link with rel='_self')."}
- {'name': 'fileSystem', 'datatype': 'String', 'description': "URI that includes the file system ID (from the link with rel='_fileSystem')."}
- {'name': 'vfs', 'datatype': 'String', 'description': "URI that includes the virtual file server ID (from the link with rel='_vfs')."}

**KPIs:**
- id
- name
- fileSystemPath
- fileSystemId
- evsId
- accessConfiguration
- snapshotOptions
- transferToReplicationTarget

---

### 34. GET https://ipAddress/v1/file/storage-systems/storageSystemId/file-systems/fileSystemId/exports/exportId
**Description:** You can get information about an export in the specified file system.
**Confidence Score:** 0.90

**Entities:**
- {'name': 'id', 'datatype': 'String', 'description': 'ID of the share.'}
- {'name': 'name', 'datatype': 'String', 'description': 'Name of the resource.'}
- {'name': 'fileSystemPath', 'datatype': 'String', 'description': 'The file system location to be accessed through the resource. Min length = 1, max length = 80.'}
- {'name': 'fileSystemId', 'datatype': 'String', 'description': 'ID of the file system. Min length = 0, max length = 256.'}
- {'name': 'evsId', 'datatype': 'Integer', 'description': 'ID of the virtual file server.'}
- {'name': 'accessConfiguration', 'datatype': 'String', 'description': 'The access security for this resource. Min length = 1, max length = 5957.'}
- {'name': 'snapshotOptions', 'datatype': 'String', 'description': 'Snapshot access options: 0 = Hides and disallows access to snapshots; 1 = Hides snapshots but allows access to hidden snapshots; 3 = Displays and allows access to snapshots.'}
- {'name': 'transferToReplicationTarget', 'datatype': 'String', 'description': 'Indicates if NFS exports are transferred to recovered file systems: 0 = Not transferred; 1 = Transferred when target file system is brought online; 2 = Transferred to recovered file systems.'}
- {'name': 'links', 'datatype': 'List', 'description': 'Displays related resources.'}
- {'name': 'links[].rel', 'datatype': 'String', 'description': 'Relationship type of the linked resource (e.g., _self, _filesystem, _vfs).'}
- {'name': 'links[].href', 'datatype': 'String', 'description': 'URI of the linked resource.'}
- {'name': 'self', 'datatype': 'String', 'description': 'URI that includes the resource ID.'}
- {'name': 'fileSystem', 'datatype': 'String', 'description': 'URI that includes the file system ID.'}
- {'name': 'evs', 'datatype': 'String', 'description': 'URI that includes the Virtual File Server ID.'}

**KPIs:**
- id
- name
- fileSystemPath
- fileSystemId
- evsId
- accessConfiguration
- snapshotOptions
- transferToReplicationTarget

---
