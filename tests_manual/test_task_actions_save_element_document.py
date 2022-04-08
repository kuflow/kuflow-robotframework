import kuflow_rest_client
from kuflow_rest_client.api import task_api
from kuflow_rest_client.model.save_element_document_command import \
    SaveElementDocumentCommand

configuration = kuflow_rest_client.Configuration(
    host="https://api.sandbox.kuflow.com/v1.0",
    username="",
    password="",
)

with kuflow_rest_client.ApiClient(configuration) as api_client:
    api_instance = task_api.TaskApi(api_client)

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
    except kuflow_rest_client.ApiException as e:
        print("Exception when calling TaskApi->actions_save_element_document: %s\n" % e)
