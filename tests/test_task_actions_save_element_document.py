import kuflow_rest_client
from kuflow_rest_client.api import task_api
from kuflow_rest_client.model.save_element_document_command import (
    SaveElementDocumentCommand,
)
from kuflow_rest_client.model.task import Task
from pprint import pprint

import logging
import contextlib


try:
    from http.client import HTTPConnection # py3
except ImportError:
    from httplib import HTTPConnection # py2

def debug_requests_on():
    '''Switches on logging of the requests module.'''
    HTTPConnection.debuglevel = 1

    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True


configuration = kuflow_rest_client.Configuration(
    host="https://api.sandbox.kuflow.com/v1.0",
    username="",
    password="",
)

# Enter a context with an instance of the API client
with kuflow_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = task_api.TaskApi(api_client)

    debug_requests_on()
    # # example passing only required values which don't have defaults set
    # path_params = {
    #     "id": "id_example",
    # }
    # try:
    #     # Save an element document
    #     api_response = api_instance.actions_save_element_document(
    #         path_params=path_params,
    #     )
    #     pprint(api_response)
    # except kuflow_rest_client.ApiException as e:
    #     print("Exception when calling TaskApi->actions_save_element_document: %s\n" % e)

    # example passing only optional values
    path_params = {
        "id": "6c09357e-6a06-3304-8592-4179a8bfd408",
    }
    body = dict(
        json=SaveElementDocumentCommand(
            code="DOC_MULTIPLE",
        ),
        file=open("/home/zeben/dummy/Demonio_de_tazmania.jpg", "rb"),
    )
    try:
        # Save an element document
        api_response = api_instance.actions_save_element_document(
            path_params=path_params,
            body=body,
        )
        #pprint(api_response)
    except kuflow_rest_client.ApiException as e:
        print("Exception when calling TaskApi->actions_save_element_document: %s\n" % e)
