import kuflow_rest_client
from kuflow_rest_client.api import authentication_api
from kuflow_rest_client.model.default_error import DefaultError
from kuflow_rest_client.model.authentication import Authentication
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = kuflow_rest_client.Configuration(
    host="https://api.sandbox.kuflow.com/v1.0",
    username="72fcb58c-5028-41e1-b4d1-417df487ade6",
    password="#:X9qHXbU5[8cKd",
)
# Enter a context with an instance of the API client
with kuflow_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentication_api.AuthenticationApi(api_client)

    # example passing only required values which don't have defaults set
    body = Authentication(type="ENGINE")
    try:
        # Create an authentication for the current principal
        api_response = api_instance.create_authentication(
            body=body,
        )
        pprint(api_response)
    except kuflow_rest_client.ApiException as e:
        print("Exception when calling AuthenticationApi->create_authentication: %s\n" % e)