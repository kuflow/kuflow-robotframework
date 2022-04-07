# kuflow_rest_client.ProcessApi

All URIs are relative to *https://api.kuflow.com/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**actions_cancel_process**](ProcessApi.md#actions_cancel_process) | **POST** /processes/{id}/~actions/cancel | Cancel a Process
[**actions_complete_process**](ProcessApi.md#actions_complete_process) | **POST** /processes/{id}/~actions/complete | Complete a Process
[**create_process**](ProcessApi.md#create_process) | **POST** /processes | Create a new process
[**find_processes**](ProcessApi.md#find_processes) | **GET** /processes | Find all accessible Processes
[**retrieve_process**](ProcessApi.md#retrieve_process) | **GET** /processes/{id} | Get a Process by Id

# **actions_cancel_process**
> Process actions_cancel_process(id)

Cancel a Process

Cancel a Process. The state of Process is setted to canceled. All the active tasks will be marked as canceled too.  If you are already in this state, no action is taken. 

### Example

* Basic Authentication (BasicAuth):
```python
import kuflow_rest_client
from kuflow_rest_client.api import process_api
from kuflow_rest_client.model.process import Process
from kuflow_rest_client.model.default_error import DefaultError
from pprint import pprint
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
    api_instance = process_api.ProcessApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    try:
        # Cancel a Process
        api_response = api_instance.actions_cancel_process(
            path_params=path_params,
        )
        pprint(api_response)
    except kuflow_rest_client.ApiException as e:
        print("Exception when calling ProcessApi->actions_cancel_process: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

#### IdSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Process cancelled 
default | ApiResponseForDefault | Unexpected error 

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Process**](Process.md) |  | 


#### ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DefaultError**](DefaultError.md) |  | 



[**Process**](Process.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_complete_process**
> Process actions_complete_process(id)

Complete a Process

Complete a Process. The state of Process is setted to completed.  If you are already in this state, no action is taken. 

### Example

* Basic Authentication (BasicAuth):
```python
import kuflow_rest_client
from kuflow_rest_client.api import process_api
from kuflow_rest_client.model.process import Process
from kuflow_rest_client.model.default_error import DefaultError
from pprint import pprint
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
    api_instance = process_api.ProcessApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    try:
        # Complete a Process
        api_response = api_instance.actions_complete_process(
            path_params=path_params,
        )
        pprint(api_response)
    except kuflow_rest_client.ApiException as e:
        print("Exception when calling ProcessApi->actions_complete_process: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

#### IdSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Process completed 
default | ApiResponseForDefault | Unexpected error 

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Process**](Process.md) |  | 


#### ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DefaultError**](DefaultError.md) |  | 



[**Process**](Process.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_process**
> Process create_process(process)

Create a new process

Creates a process. This option has direct correspondence to the action of starting a process in the Kuflow GUI.  If you want the method to be idempotent, please specify the `id` field in the request body. 

### Example

* Basic Authentication (BasicAuth):
```python
import kuflow_rest_client
from kuflow_rest_client.api import process_api
from kuflow_rest_client.model.process import Process
from kuflow_rest_client.model.default_error import DefaultError
from pprint import pprint
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
    api_instance = process_api.ProcessApi(api_client)

    # example passing only required values which don't have defaults set
    body = Process()
    try:
        # Create a new process
        api_response = api_instance.create_process(
            body=body,
        )
        pprint(api_response)
    except kuflow_rest_client.ApiException as e:
        print("Exception when calling ProcessApi->create_process: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Process**](Process.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Process already created 
201 | ApiResponseFor201 | Process created 
default | ApiResponseForDefault | Unexpected error 

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Process**](Process.md) |  | 


#### ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Process**](Process.md) |  | 


#### ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DefaultError**](DefaultError.md) |  | 



[**Process**](Process.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_processes**
> ProcessPage find_processes()

Find all accessible Processes

List all the Processes that have been created and the the credentials has access.

### Example

* Basic Authentication (BasicAuth):
```python
import kuflow_rest_client
from kuflow_rest_client.api import process_api
from kuflow_rest_client.model.default_error import DefaultError
from kuflow_rest_client.model.process_page import ProcessPage
from pprint import pprint
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
    api_instance = process_api.ProcessApi(api_client)

    # example passing only optional values
    query_params = {
        'size': 25,
        'page': 0,
    }
    try:
        # Find all accessible Processes
        api_response = api_instance.find_processes(
            query_params=query_params,
        )
        pprint(api_response)
    except kuflow_rest_client.ApiException as e:
        print("Exception when calling ProcessApi->find_processes: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
size | SizeSchema | | optional
page | PageSchema | | optional


#### SizeSchema

Type | Description | Notes
------------- | ------------- | -------------
**int** |  | defaults to 25

#### PageSchema

Type | Description | Notes
------------- | ------------- | -------------
**int** |  | defaults to 0

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Processes found paginated 
default | ApiResponseForDefault | Unexpected error 

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProcessPage**](ProcessPage.md) |  | 


#### ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DefaultError**](DefaultError.md) |  | 



[**ProcessPage**](ProcessPage.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_process**
> Process retrieve_process(id)

Get a Process by Id

Returns the requested Process when has access to do it.

### Example

* Basic Authentication (BasicAuth):
```python
import kuflow_rest_client
from kuflow_rest_client.api import process_api
from kuflow_rest_client.model.process import Process
from kuflow_rest_client.model.default_error import DefaultError
from pprint import pprint
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
    api_instance = process_api.ProcessApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    try:
        # Get a Process by Id
        api_response = api_instance.retrieve_process(
            path_params=path_params,
        )
        pprint(api_response)
    except kuflow_rest_client.ApiException as e:
        print("Exception when calling ProcessApi->retrieve_process: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

#### IdSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Successful operation 
default | ApiResponseForDefault | Unexpected error 

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Process**](Process.md) |  | 


#### ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DefaultError**](DefaultError.md) |  | 



[**Process**](Process.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

