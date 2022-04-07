# coding: utf-8

"""
    KuFlow Public API

    # Introduction This document contains the KuFlow REST API reference. This API is a fundamental part in the integration of external systems with KuFlow and is used, among others, by the different implementations of the Workers that connect to our network.  # API Versioning  A versioning strategy allows our clients to continue using the existing REST API and migrate their applications to the newer API when they are ready.  The scheme followed is a simplification of *Semver* where only MAJOR versions are differentiated from MINOR or PATCH versions, i.e. a version number of only two levels is used. With this approach, you only have to migrate your applications if you want to upgrade to a MAJOR version of the KuFlow API. In case you want to upgrade to a MINOR version, you can do so without any incompatibility issues.  The versioning of the api is done through the URI Path, that is, the version number is included in the URI Path. The URL structure would be as follows:  ```bash https://{endpoint}/vMAJOR.MINOR/{api-path} ```  # Idempotency  The API is designed to support idempotency in order to achieve a correct resilience in the implementation of its clients. The way to achieve this is very simple, in the methods that create resources, you simply have to specify a UUID in the input data and the API will respond by creating or returning the resource if it previously existed. With this mechanism, your systems can implement retry logic without worrying about performing data tradeoffs.  # OpenAPI Specification  This API is documented in OpenAPI format. This file allows you to create REST clients with the technology of your choice automatically. In our code repositories you can find an example of this automation using Feign for JAVA.   # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: kuflow@kuflow.com
    Generated by: https://openapi-generator.tech
"""

import re  # noqa: F401
import sys  # noqa: F401
import typing  # noqa: F401

from frozendict import frozendict  # noqa: F401

import decimal  # noqa: F401
from datetime import date, datetime  # noqa: F401
from frozendict import frozendict  # noqa: F401

from kuflow_rest_client.schemas import (  # noqa: F401
    AnyTypeSchema,
    ComposedSchema,
    DictSchema,
    ListSchema,
    StrSchema,
    IntSchema,
    Int32Schema,
    Int64Schema,
    Float32Schema,
    Float64Schema,
    NumberSchema,
    DateSchema,
    DateTimeSchema,
    DecimalSchema,
    BoolSchema,
    BinarySchema,
    NoneSchema,
    none_type,
    InstantiationMetadata,
    Unset,
    unset,
    ComposedBase,
    ListBase,
    DictBase,
    NoneBase,
    StrBase,
    IntBase,
    NumberBase,
    DateBase,
    DateTimeBase,
    BoolBase,
    BinaryBase,
    Schema,
    _SchemaValidator,
    _SchemaTypeChecker,
    _SchemaEnumMaker,
)


class TaskPage(ComposedSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    @classmethod
    @property
    def _composed_schemas(cls):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        return {
            "allOf": [
                Page,
                TaskPageAllOf,
            ],
            "oneOf": [],
            "anyOf": [],
        }

    def __new__(
        cls,
        *args: typing.Union[
            dict,
            frozendict,
            str,
            date,
            datetime,
            int,
            float,
            decimal.Decimal,
            None,
            list,
            tuple,
            bytes,
        ],
        _instantiation_metadata: typing.Optional[InstantiationMetadata] = None,
        **kwargs: typing.Type[Schema],
    ) -> "TaskPage":
        return super().__new__(
            cls,
            *args,
            _instantiation_metadata=_instantiation_metadata,
            **kwargs,
        )


from kuflow_rest_client.model.page import Page
from kuflow_rest_client.model.task_page_all_of import TaskPageAllOf
