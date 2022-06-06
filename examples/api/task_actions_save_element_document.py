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
from kuflow_rest_client.model.save_element_value_document_command import (
    SaveElementValueDocumentCommand,
)

configuration = kuflow_rest_client.Configuration(
    host="https://api.kuflow.com/v1.0",
    username="",
    password="",
)

with kuflow_rest_client.ApiClient(configuration) as api_client:
    api_instance = task_api.TaskApi(api_client)

    path_params = {
        "id": "adc7672e-299c-3bbf-906a-bda7c255e1e4",
    }
    body = dict(
        json=SaveElementValueDocumentCommand(
            code="DOC_MULTIPLE",
        ),
        file=open("/home/user/file.jpg", "rb"),
    )
    try:
        # Save an element document
        api_response = api_instance.actions_save_element_value_document(
            path_params=path_params,
            body=body,
        )
    except kuflow_rest_client.ApiException as e:
        print("Exception when calling TaskApi->actions_save_element_document: %s\n" % e)
