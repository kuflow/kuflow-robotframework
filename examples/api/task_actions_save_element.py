#
# MIT License
#
# Copyright (c) 2022 KuFlow
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.#


import kuflow_rest_client
import time

from kuflow_rest_client.api import task_api
from kuflow_rest_client.model.task_element_value_or_array_value import TaskTaskElementValueOrArrayValue

configuration = kuflow_rest_client.Configuration(
    host="https://api.sandbox.kuflow.com/v1.0",
    username="72fcb58c-5028-41e1-b4d1-417df487ade6",
    password="#:X9qHXbU5[8cKd",
)

with kuflow_rest_client.ApiClient(configuration) as api_client:
    api_instance = task_api.TaskApi(api_client)

    path_params = {
        "id": "f5cea8a2-1b37-3c55-b942-a358f793e83f",
    }

    time = time.strftime("%a, %d %b %Y %H:%M:%S %Z(%z)")

    elementValueOne = {"value": "Example Value " + time, "valid": False}
    # SINGLE ELEMENT
    body_single = TaskTaskElementValueOrArrayValue(
        code="FIELD",
        value=TaskTaskElementValueOrArrayValue.value(elementValueOne),
    )

    # MULTI ELEMENT
    elementValueTwo = elementValueOne.copy()
    elementValueTwo["value"] = "Another Example " + time
    valueList = [elementValueOne, elementValueTwo]
    body_multiple = TaskTaskElementValueOrArrayValue(
        code="FIELD_MULTIPLE",
        value=TaskTaskElementValueOrArrayValue.value(valueList),
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
