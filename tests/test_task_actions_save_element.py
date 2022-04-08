import kuflow_rest_client
import time

from kuflow_rest_client.api import task_api
# from kuflow_rest_client.model.default_error import DefaultError
from kuflow_rest_client.model.element_value_or_array_value import ElementValueOrArrayValue
# from kuflow_rest_client.model.task import Task
# from pprint import pprint
# from kuflow_rest_client.model.task_element_value import TaskElementValue

configuration = kuflow_rest_client.Configuration(
    host="https://api.sandbox.kuflow.com/v1.0",
    username="72fcb58c-5028-41e1-b4d1-417df487ade6",
    password="#:X9qHXbU5[8cKd",
)

# Enter a context with an instance of the API client
with kuflow_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = task_api.TaskApi(api_client)

    path_params = {
        'id': "6c09357e-6a06-3304-8592-4179a8bfd408",
    }

    time = time.strftime('%a, %d %b %Y %H:%M:%S %Z(%z)')

    elementValue = {"value": "Example Value " + time}
    # SINGLE ELEMENT
    body = ElementValueOrArrayValue(
        code="FIELD",
        value=ElementValueOrArrayValue.value(elementValue),
    )

    # MULTI ELEMENT
    elementValue2 = elementValue.copy()
    elementValue2["value"] = "Another Example" + time
    valueList = [elementValue, elementValue2]
    body_multiple = ElementValueOrArrayValue(
        code="FIELD_MULTIPLE",
        value=ElementValueOrArrayValue.value(valueList),
    )

    try:
        # Save an element
        api_response = api_instance.actions_save_element(
            path_params=path_params,
            body=body,
        )

        # Save an element multiple
        api_response = api_instance.actions_save_element(
            path_params=path_params,
            body=body_multiple,
        )

        # pprint(api_response)
    except kuflow_rest_client.ApiException as e:
        print("Exception when calling TaskApi->actions_save_element: %s\n" % e)
