import kuflow_rest_client
from kuflow_rest_client.api import task_api
from kuflow_rest_client.model.default_error import DefaultError
from kuflow_rest_client.model.element_value_or_array_value import ElementValueOrArrayValue
from kuflow_rest_client.model.task import Task
from pprint import pprint

from kuflow_rest_client.model.task_element_value import TaskElementValue

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
        'id': "6c09357e-6a06-3304-8592-4179a8bfd408",
    }

    body = ElementValueOrArrayValue(
        code="FIELD",
        value=ElementValueOrArrayValue.value(value='Mi valor de ejemplo'),
    )
    try:
        # Save an element
        api_response = api_instance.actions_save_element(
            path_params=path_params,
            body=body,
        )
        # pprint(api_response)
    except kuflow_rest_client.ApiException as e:
        print("Exception when calling TaskApi->actions_save_element: %s\n" % e)
