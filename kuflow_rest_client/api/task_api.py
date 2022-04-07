# coding: utf-8

"""
    KuFlow Public API

    # Introduction This document contains the KuFlow REST API reference. This API is a fundamental part in the integration of external systems with KuFlow and is used, among others, by the different implementations of the Workers that connect to our network.  # API Versioning  A versioning strategy allows our clients to continue using the existing REST API and migrate their applications to the newer API when they are ready.  The scheme followed is a simplification of *Semver* where only MAJOR versions are differentiated from MINOR or PATCH versions, i.e. a version number of only two levels is used. With this approach, you only have to migrate your applications if you want to upgrade to a MAJOR version of the KuFlow API. In case you want to upgrade to a MINOR version, you can do so without any incompatibility issues.  The versioning of the api is done through the URI Path, that is, the version number is included in the URI Path. The URL structure would be as follows:  ```bash https://{endpoint}/vMAJOR.MINOR/{api-path} ```  # Idempotency  The API is designed to support idempotency in order to achieve a correct resilience in the implementation of its clients. The way to achieve this is very simple, in the methods that create resources, you simply have to specify a UUID in the input data and the API will respond by creating or returning the resource if it previously existed. With this mechanism, your systems can implement retry logic without worrying about performing data tradeoffs.  # OpenAPI Specification  This API is documented in OpenAPI format. This file allows you to create REST clients with the technology of your choice automatically. In our code repositories you can find an example of this automation using Feign for JAVA.   # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: kuflow@kuflow.com
    Generated by: https://openapi-generator.tech
"""

from kuflow_rest_client.api_client import ApiClient
from kuflow_rest_client.api.task_api_endpoints.actions_append_log import (
    ActionsAppendLog,
)
from kuflow_rest_client.api.task_api_endpoints.actions_assign_task import (
    ActionsAssignTask,
)
from kuflow_rest_client.api.task_api_endpoints.actions_claim_task import (
    ActionsClaimTask,
)
from kuflow_rest_client.api.task_api_endpoints.actions_complete_task import (
    ActionsCompleteTask,
)
from kuflow_rest_client.api.task_api_endpoints.actions_delete_document import (
    ActionsDeleteDocument,
)
from kuflow_rest_client.api.task_api_endpoints.actions_delete_element import (
    ActionsDeleteElement,
)
from kuflow_rest_client.api.task_api_endpoints.actions_download_element_document import (
    ActionsDownloadElementDocument,
)
from kuflow_rest_client.api.task_api_endpoints.actions_save_element import (
    ActionsSaveElement,
)
from kuflow_rest_client.api.task_api_endpoints.create_task import CreateTask
from kuflow_rest_client.api.task_api_endpoints.find_tasks import FindTasks
from kuflow_rest_client.api.task_api_endpoints.retrieve_task import RetrieveTask


class TaskApi(
    ActionsAppendLog,
    ActionsAssignTask,
    ActionsClaimTask,
    ActionsCompleteTask,
    ActionsDeleteDocument,
    ActionsDeleteElement,
    ActionsDownloadElementDocument,
    ActionsSaveElement,
    CreateTask,
    FindTasks,
    RetrieveTask,
    ApiClient,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    pass
