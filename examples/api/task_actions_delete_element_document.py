import kuflow_rest_client
from kuflow_rest_client.api import task_api
from kuflow_rest_client.model.delete_element_document_command import DeleteElementDocumentCommand

configuration = kuflow_rest_client.Configuration(
    host="https://api.kuflow.com/v1.0",
    username="",
    password="",
)

with kuflow_rest_client.ApiClient(configuration) as api_client:
    api_instance = task_api.TaskApi(api_client)

    path_params = {
        "id": "0ccf164b-e150-328e-8a86-9d5be73972f1",
    }

    body = DeleteElementDocumentCommand(
        documentId="79fdcd62-14f4-4789-8957-085297f4615a",
    )

    try:
        # Delete an element document value
        api_response = api_instance.actions_delete_document(
            path_params=path_params,
            body=body,
        )
    except kuflow_rest_client.ApiException as e:
        print("Exception when calling TaskApi->actions_delete_document: %s\n" % e)
