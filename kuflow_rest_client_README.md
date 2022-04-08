# kuflow-rest-client
# Introduction This document contains the KuFlow REST API reference. This API is a fundamental part in the integration of external systems with KuFlow and is used, among others, by the different implementations of the Workers that connect to our network.  # API Versioning  A versioning strategy allows our clients to continue using the existing REST API and migrate their applications to the newer API when they are ready.  The scheme followed is a simplification of *Semver* where only MAJOR versions are differentiated from MINOR or PATCH versions, i.e. a version number of only two levels is used. With this approach, you only have to migrate your applications if you want to upgrade to a MAJOR version of the KuFlow API. In case you want to upgrade to a MINOR version, you can do so without any incompatibility issues.  The versioning of the api is done through the URI Path, that is, the version number is included in the URI Path. The URL structure would be as follows:  ```bash https://{endpoint}/vMAJOR.MINOR/{api-path} ```  # Idempotency  The API is designed to support idempotency in order to achieve a correct resilience in the implementation of its clients. The way to achieve this is very simple, in the methods that create resources, you simply have to specify a UUID in the input data and the API will respond by creating or returning the resource if it previously existed. With this mechanism, your systems can implement retry logic without worrying about performing data tradeoffs.  # OpenAPI Specification  This API is documented in OpenAPI format. This file allows you to create REST clients with the technology of your choice automatically. In our code repositories you can find an example of this automation using Feign for JAVA. 

The `kuflow_rest_client` package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0
- Package version: 0.1.0
- Build package: org.openapitools.codegen.languages.PythonExperimentalClientCodegen

## Requirements.

Python &gt;&#x3D;3.9

## Installation & Usage

This python library package is generated without supporting files like setup.py or requirements files

To be able to use it, you will need these dependencies in your own package that uses this library:

* urllib3 >= 1.15
* certifi
* python-dateutil

## Getting Started

In your own code, to use this library to connect and interact with kuflow-rest-client,
you can run the following:

```python

import time
import kuflow_rest_client
from pprint import pprint
from kuflow_rest_client.api import authentication_api
from kuflow_rest_client.model.authentication import Authentication
from kuflow_rest_client.model.default_error import DefaultError
# Defining the host is optional and defaults to https://api.kuflow.com/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = kuflow_rest_client.Configuration(
    host = "https://api.kuflow.com/v1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = kuflow_rest_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with kuflow_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentication_api.AuthenticationApi(api_client)
    authentication = Authentication() # Authentication | 

    try:
        # Create an authentication for the current principal
        api_response = api_instance.create_authentication(authentication)
        pprint(api_response)
    except kuflow_rest_client.ApiException as e:
        print("Exception when calling AuthenticationApi->create_authentication: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.kuflow.com/v1.0*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthenticationApi* | [**create_authentication**](kuflow_rest_client/docs/AuthenticationApi.md#create_authentication) | **POST** /authentications | Create an authentication for the current principal
*ProcessApi* | [**actions_cancel_process**](kuflow_rest_client/docs/ProcessApi.md#actions_cancel_process) | **POST** /processes/{id}/~actions/cancel | Cancel a Process
*ProcessApi* | [**actions_complete_process**](kuflow_rest_client/docs/ProcessApi.md#actions_complete_process) | **POST** /processes/{id}/~actions/complete | Complete a Process
*ProcessApi* | [**create_process**](kuflow_rest_client/docs/ProcessApi.md#create_process) | **POST** /processes | Create a new process
*ProcessApi* | [**find_processes**](kuflow_rest_client/docs/ProcessApi.md#find_processes) | **GET** /processes | Find all accessible Processes
*ProcessApi* | [**retrieve_process**](kuflow_rest_client/docs/ProcessApi.md#retrieve_process) | **GET** /processes/{id} | Get a Process by Id
*TaskApi* | [**actions_append_log**](kuflow_rest_client/docs/TaskApi.md#actions_append_log) | **POST** /tasks/{id}/~actions/append-log | Append a log to the task
*TaskApi* | [**actions_assign_task**](kuflow_rest_client/docs/TaskApi.md#actions_assign_task) | **POST** /tasks/{id}/~actions/assign | Assign a task
*TaskApi* | [**actions_claim_task**](kuflow_rest_client/docs/TaskApi.md#actions_claim_task) | **POST** /tasks/{id}/~actions/claim | Claim a task
*TaskApi* | [**actions_complete_task**](kuflow_rest_client/docs/TaskApi.md#actions_complete_task) | **POST** /tasks/{id}/~actions/complete | Complete a task
*TaskApi* | [**actions_delete_document**](kuflow_rest_client/docs/TaskApi.md#actions_delete_document) | **POST** /tasks/{id}/~actions/delete-element-document | Delete an element document value
*TaskApi* | [**actions_delete_element**](kuflow_rest_client/docs/TaskApi.md#actions_delete_element) | **POST** /tasks/{id}/~actions/delete-element | Delete an element by code
*TaskApi* | [**actions_download_element_document**](kuflow_rest_client/docs/TaskApi.md#actions_download_element_document) | **GET** /tasks/{id}/~actions/download-element-document | Download document
*TaskApi* | [**actions_save_element**](kuflow_rest_client/docs/TaskApi.md#actions_save_element) | **POST** /tasks/{id}/~actions/save-element | Save an element
*TaskApi* | [**actions_save_element_document**](kuflow_rest_client/docs/TaskApi.md#actions_save_element_document) | **POST** /tasks/{id}/~actions/save-element-document | Save an element document
*TaskApi* | [**create_task**](kuflow_rest_client/docs/TaskApi.md#create_task) | **POST** /tasks | Create a new Task in the selected Process
*TaskApi* | [**find_tasks**](kuflow_rest_client/docs/TaskApi.md#find_tasks) | **GET** /tasks | Find all accessible Taks
*TaskApi* | [**retrieve_task**](kuflow_rest_client/docs/TaskApi.md#retrieve_task) | **GET** /tasks/{id} | Get a task given it Id

## Documentation For Models

 - [AbstractAudited](kuflow_rest_client/docs/AbstractAudited.md)
 - [AssignTaskCommand](kuflow_rest_client/docs/AssignTaskCommand.md)
 - [Authentication](kuflow_rest_client/docs/Authentication.md)
 - [AuthenticationAllOf](kuflow_rest_client/docs/AuthenticationAllOf.md)
 - [AuthenticationType](kuflow_rest_client/docs/AuthenticationType.md)
 - [DefaultError](kuflow_rest_client/docs/DefaultError.md)
 - [DefaultErrorInfo](kuflow_rest_client/docs/DefaultErrorInfo.md)
 - [DeleteElementCommand](kuflow_rest_client/docs/DeleteElementCommand.md)
 - [DeleteElementDocumentCommand](kuflow_rest_client/docs/DeleteElementDocumentCommand.md)
 - [ElementDefinitionType](kuflow_rest_client/docs/ElementDefinitionType.md)
 - [ElementValueDocument](kuflow_rest_client/docs/ElementValueDocument.md)
 - [ElementValueOrArrayValue](kuflow_rest_client/docs/ElementValueOrArrayValue.md)
 - [Log](kuflow_rest_client/docs/Log.md)
 - [LogLevel](kuflow_rest_client/docs/LogLevel.md)
 - [Page](kuflow_rest_client/docs/Page.md)
 - [PageMetadata](kuflow_rest_client/docs/PageMetadata.md)
 - [Principal](kuflow_rest_client/docs/Principal.md)
 - [PrincipalType](kuflow_rest_client/docs/PrincipalType.md)
 - [Process](kuflow_rest_client/docs/Process.md)
 - [ProcessAllOf](kuflow_rest_client/docs/ProcessAllOf.md)
 - [ProcessDefinitionSummary](kuflow_rest_client/docs/ProcessDefinitionSummary.md)
 - [ProcessElementValue](kuflow_rest_client/docs/ProcessElementValue.md)
 - [ProcessPage](kuflow_rest_client/docs/ProcessPage.md)
 - [ProcessPageAllOf](kuflow_rest_client/docs/ProcessPageAllOf.md)
 - [ProcessState](kuflow_rest_client/docs/ProcessState.md)
 - [Task](kuflow_rest_client/docs/Task.md)
 - [TaskAllOf](kuflow_rest_client/docs/TaskAllOf.md)
 - [TaskElementValue](kuflow_rest_client/docs/TaskElementValue.md)
 - [TaskPage](kuflow_rest_client/docs/TaskPage.md)
 - [TaskPageAllOf](kuflow_rest_client/docs/TaskPageAllOf.md)
 - [TaskState](kuflow_rest_client/docs/TaskState.md)
 - [TasksDefinitionSummary](kuflow_rest_client/docs/TasksDefinitionSummary.md)
 - [WebhookEvent](kuflow_rest_client/docs/WebhookEvent.md)
 - [WebhookEventProcessStateChanged](kuflow_rest_client/docs/WebhookEventProcessStateChanged.md)
 - [WebhookEventProcessStateChangedAllOf](kuflow_rest_client/docs/WebhookEventProcessStateChangedAllOf.md)
 - [WebhookEventProcessStateChangedData](kuflow_rest_client/docs/WebhookEventProcessStateChangedData.md)
 - [WebhookEventTaskStateChanged](kuflow_rest_client/docs/WebhookEventTaskStateChanged.md)
 - [WebhookEventTaskStateChangedAllOf](kuflow_rest_client/docs/WebhookEventTaskStateChangedAllOf.md)
 - [WebhookEventTaskStateChangedData](kuflow_rest_client/docs/WebhookEventTaskStateChangedData.md)
 - [WebhookType](kuflow_rest_client/docs/WebhookType.md)

## Documentation For Authorization

 Authentication schemes defined for the API:
## BasicAuth

- **Type**: HTTP basic authentication


## Author

kuflow@kuflow.com
kuflow@kuflow.com
kuflow@kuflow.com

## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in kuflow_rest_client.apis and kuflow_rest_client.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from kuflow_rest_client.api.default_api import DefaultApi`
- `from kuflow_rest_client.model.pet import Pet`

Solution 1:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import kuflow_rest_client
from kuflow_rest_client.apis import *
from kuflow_rest_client.models import *
```