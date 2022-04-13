import kuflow_rest_client
import time

from kuflow_rest_client.api import task_api
from kuflow_rest_client.model.element_value_or_array_value import ElementValueOrArrayValue

configuration = kuflow_rest_client.Configuration(
    host="https://api.kuflow.com/v1.0",
    username="",
    password="",
)

with kuflow_rest_client.ApiClient(configuration) as api_client:
    api_instance = task_api.TaskApi(api_client)

    path_params = {
        'id': "eef6d86f-93d7-4c7c-85bd-948bc7c95720",
    }

    time = time.strftime('%a, %d %b %Y %H:%M:%S %Z(%z)')

    elementValueOne = {"value": "Example Value " + time, "valid": False}
    # SINGLE ELEMENT
    body_single = ElementValueOrArrayValue(
        code="FIELD",
        value=ElementValueOrArrayValue.value(elementValueOne),
    )

    # MULTI ELEMENT
    elementValueTwo = elementValueOne.copy()
    elementValueTwo["value"] = "Another Example" + time
    valueList = [elementValueOne, elementValueTwo]
    body_multiple = ElementValueOrArrayValue(
        code="FIELD_MULTIPLE",
        value=ElementValueOrArrayValue.value(valueList),
    )

    try:
        # Save an element
        api_response = api_instance.actions_save_element(
            path_params=path_params,
            body=body_single,
        )

        # Save an element multiple
        api_response = api_instance.actions_save_element(
            path_params=path_params,
            body=body_multiple,
        )
    except kuflow_rest_client.ApiException as e:
        print("Exception when calling TaskApi->actions_save_element: %s\n" % e)