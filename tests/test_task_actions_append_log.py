import kuflow_rest_client
from kuflow_rest_client.api import task_api
from kuflow_rest_client.model.log import Log
from kuflow_rest_client.model.log_level import LogLevel
from kuflow_rest_client.model.task import Task
from pprint import pprint

# Defining the host is optional and defaults to https://api.kuflow.com/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = kuflow_rest_client.Configuration(host="https://api.kuflow.com/v1.0")

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = kuflow_rest_client.Configuration(
    host="https://api.sandbox.kuflow.com/v1.0",
    username="",
    password="",
)
# Enter a context with an instance of the API client
with kuflow_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = task_api.TaskApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        "id": "b62bbe25-cd7c-315b-bcc8-1d6303fee671",
    }
    body = Log(
        message="message_example_3",
        level=LogLevel("INFO"),
    )
    try:
        # Append a log to the task
        api_response = api_instance.actions_append_log(
            path_params=path_params,
            body=body,
        )
   #     pprint(api_response)
    except kuflow_rest_client.ApiException as e:
        print("Exception when calling TaskApi->actions_append_log: %s\n" % e)
