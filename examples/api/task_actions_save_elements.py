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

from kuflow_rest_client.api import task_api
from kuflow_rest_client.model.element_value_or_array_value import (
    ElementValueOrArrayValue,
)

configuration = kuflow_rest_client.Configuration(
    host="https://api.kuflow.com/v1.0",
    username="",
    password="",
)


def make_request(body):
    with kuflow_rest_client.ApiClient(configuration) as api_client:
        api_instance = task_api.TaskApi(api_client)

        path_params = {
            "id": "458fd52a-2b61-33f0-a2fc-1e164df210c1",
        }

        try:
            api_instance.actions_save_element(
                path_params=path_params,
                body=body,
            )
        except kuflow_rest_client.ApiException as e:
            print("Exception when calling TaskApi->actions_save_element: %s\n" % e)


# FIELD
body = ElementValueOrArrayValue(
    code="FIELD",
    value=ElementValueOrArrayValue.value({"value": "Hi", "valid": False}),
)
make_request(body)

# FIELD MULTIPLE
body = ElementValueOrArrayValue(
    code="FIELD_MULTIPLE",
    value=ElementValueOrArrayValue.value(
        [{"value": "Hi", "valid": False}, {"value": "Bye", "valid": False}]
    ),
)
make_request(body)

# FORM
body = ElementValueOrArrayValue(
    code="FORM",
    value=ElementValueOrArrayValue.value({"value": {"mykey": 3}, "valid": False}),
)
make_request(body)

# FORM MULTIPLE
body = ElementValueOrArrayValue(
    code="FORM_MULTIPLE",
    value=ElementValueOrArrayValue.value(
        [
            {"value": {"mykey": 3}, "valid": False},
            {"value": {"mykey": 4}, "valid": False},
        ]
    ),
)
make_request(body)

# DECISION
body = ElementValueOrArrayValue(
    code="DECISION",
    value=ElementValueOrArrayValue.value({"value": "A", "valid": False}),
)
make_request(body)

# DECISION MULTIPLE
body = ElementValueOrArrayValue(
    code="DECISION_MULTIPLE",
    value=ElementValueOrArrayValue.value(
        [{"value": "A", "valid": False}, {"value": "B", "valid": False}]
    ),
)
make_request(body)
