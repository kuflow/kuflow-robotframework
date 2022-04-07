# kuflow_rest_client.AuthenticationApi

All URIs are relative to *https://api.kuflow.com/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_authentication**](AuthenticationApi.md#create_authentication) | **POST** /authentications | Create an authentication for the current principal

# **create_authentication**
> Authentication create_authentication(authentication)

Create an authentication for the current principal

### Example

* Basic Authentication (BasicAuth):
```python
import kuflow_rest_client
from kuflow_rest_client.api import authentication_api
from kuflow_rest_client.model.default_error import DefaultError
from kuflow_rest_client.model.authentication import Authentication
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
    api_instance = authentication_api.AuthenticationApi(api_client)

    # example passing only required values which don't have defaults set
    body = Authentication()
    try:
        # Create an authentication for the current principal
        api_response = api_instance.create_authentication(
            body=body,
        )
        pprint(api_response)
    except kuflow_rest_client.ApiException as e:
        print("Exception when calling AuthenticationApi->create_authentication: %s\n" % e)
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
[**Authentication**](Authentication.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Authentication Created 
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
[**Authentication**](Authentication.md) |  | 


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



[**Authentication**](Authentication.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

