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


from frozendict import frozendict
import kuflow_rest_client

from kuflow_rest_client.api import task_api
from kuflow_rest_client.model.principal_type import PrincipalType
from kuflow_rest_client.model.task_element_value_document import TaskElementValueDocument
from kuflow_rest_client.model.task_element_value_document_item import TaskElementValueDocumentItem
from kuflow_rest_client.model.task_element_value_object import TaskElementValueObject
from kuflow_rest_client.model.task_element_value_or_array_value import TaskElementValueOrArrayValue
from kuflow_rest_client.model.task_element_value_principal import TaskElementValuePrincipal
from kuflow_rest_client.model.task_element_value_principal_item import TaskElementValuePrincipalItem
from kuflow_rest_client.model.task_element_value_string import TaskElementValueString
from kuflow_rest_client.model.task_element_value_type import TaskElementValueType

configuration = kuflow_rest_client.Configuration(
    host="https://api.kuflow.com/v1.0",
    username="",
    password="",
)


def make_request(body):
    with kuflow_rest_client.ApiClient(configuration) as api_client:
        api_instance = task_api.TaskApi(api_client)

        path_params = {
            "id": "adc7672e-299c-3bbf-906a-bda7c255e1e4",
        }

        try:
            api_instance.actions_save_element(
                path_params=path_params,
                body=body,
            )
        except kuflow_rest_client.ApiException as e:
            print("Exception when calling TaskApi->actions_save_element: %s\n" % e)


# FIELD
value = TaskElementValueString(value="Hi!", type=TaskElementValueType.STRING, valid=False)
body = TaskElementValueOrArrayValue(
    code="FIELD",
    value=frozendict(value),
)
make_request(body)

# FIELD MULTIPLE
value = TaskElementValueString(value="Hi!", type=TaskElementValueType.STRING, valid=False)
value_two = TaskElementValueString(value="Bye!", type=TaskElementValueType.STRING, valid=False)
body = TaskElementValueOrArrayValue(
    code="FIELD_MULTIPLE",
    value=[frozendict(value), frozendict(value_two)],
)
make_request(body)

# FORM
value = TaskElementValueObject(value={"mykey": 1}, type=TaskElementValueType.OBJECT, valid=False)
body = TaskElementValueOrArrayValue(
    code="FORM",
    value=frozendict(value),
)
make_request(body)

# FORM MULTIPLE
value = TaskElementValueObject(value={"mykey": "A"}, type=TaskElementValueType.OBJECT, valid=False)
value_two = TaskElementValueObject(value={"mykey": "B"}, type=TaskElementValueType.OBJECT, valid=False)
body = TaskElementValueOrArrayValue(
    code="FORM_MULTIPLE",
    value=[frozendict(value), frozendict(value_two)],
)
make_request(body)

# DECISION
value = TaskElementValueString(value="A", type=TaskElementValueType.STRING, valid=False)
body = TaskElementValueOrArrayValue(
    code="DECISION",
    value=frozendict(value),
)
make_request(body)

# DECISION MULTIPLE
value = TaskElementValueString(value="A", type=TaskElementValueType.STRING, valid=False)
value_two = TaskElementValueString(value="B", type=TaskElementValueType.STRING, valid=False)
body = TaskElementValueOrArrayValue(
    code="DECISION_MULTIPLE",
    value=[frozendict(value), frozendict(value_two)],
)
make_request(body)


# PRINCIPAL
valueItem = TaskElementValuePrincipalItem(id="8934b169-c85e-4e05-9580-13ace7f267f5", type=PrincipalType.USER)
value = TaskElementValuePrincipal(value=frozendict(valueItem), type=TaskElementValueType.PRINCIPAL, valid=False)
body = TaskElementValueOrArrayValue(
    code="PRINCIPAL",
    value=frozendict(value),
)
make_request(body)

# PRINCIPAL MULTIPLE
valueItem = TaskElementValuePrincipalItem(id="8934b169-c85e-4e05-9580-13ace7f267f5", type=PrincipalType.USER)
value = TaskElementValuePrincipal(value=frozendict(valueItem), type=TaskElementValueType.PRINCIPAL, valid=False)
valueItem_two = TaskElementValuePrincipalItem(id="8934b169-c85e-4e05-9580-13ace7f267f5", type=PrincipalType.USER)
value_two = TaskElementValuePrincipal(value=frozendict(valueItem_two), type=TaskElementValueType.PRINCIPAL, valid=False)
body = TaskElementValueOrArrayValue(
    code="PRINCIPAL_MULTIPLE",
    value=[frozendict(value), frozendict(value_two)],
)
make_request(body)


# DOCUMENT (By reference)
valueItem = TaskElementValueDocumentItem(id="ku:task/adc7672e-299c-3bbf-906a-bda7c255e1e4/element-value/eb072007-cb16-4ecd-9c58-5703e862348e")
value = TaskElementValueDocument(value=frozendict(valueItem), type=TaskElementValueType.DOCUMENT, valid=False)
body = TaskElementValueOrArrayValue(
    code="DOC",
    value=frozendict(value),
)
make_request(body)

# DOCUMENT MULTIPLE (By reference)
valueItem = TaskElementValueDocumentItem(id="ku:task/adc7672e-299c-3bbf-906a-bda7c255e1e4/element-value/eb072007-cb16-4ecd-9c58-5703e862348e")
value = TaskElementValueDocument(value=frozendict(valueItem), type=TaskElementValueType.DOCUMENT, valid=False)
valueItem_two = TaskElementValueDocumentItem(id="ku:task/adc7672e-299c-3bbf-906a-bda7c255e1e4/element-value/c912d2e9-e41c-4f84-8454-720d86acfd9c")
value_two = TaskElementValueDocument(value=frozendict(valueItem_two), type=TaskElementValueType.DOCUMENT, valid=False)
body = TaskElementValueOrArrayValue(
    code="DOC_MULTIPLE",
    value=[frozendict(value), frozendict(value_two)],
)
make_request(body)
