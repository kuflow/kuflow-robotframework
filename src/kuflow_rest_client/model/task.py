# coding: utf-8
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
import functools  # noqa: F401

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
    UUIDSchema,
    DateSchema,
    DateTimeSchema,
    DecimalSchema,
    BoolSchema,
    BinarySchema,
    NoneSchema,
    none_type,
    Configuration,
    Unset,
    unset,
    ComposedBase,
    ListBase,
    DictBase,
    NoneBase,
    StrBase,
    IntBase,
    Int32Base,
    Int64Base,
    Float32Base,
    Float64Base,
    NumberBase,
    UUIDBase,
    DateBase,
    DateTimeBase,
    BoolBase,
    BinaryBase,
    Schema,
    _SchemaValidator,
    _SchemaTypeChecker,
    _SchemaEnumMaker,
)


class Task(ComposedSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    @classmethod
    @property
    @functools.cache
    def _composed_schemas(cls):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading

        class allOf_1(DictSchema):
            _required_property_names = set(())
            id = UUIDSchema

            class state(ComposedSchema):
                @classmethod
                @property
                @functools.cache
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
                            TaskState,
                        ],
                        "oneOf": [],
                        "anyOf": [],
                        "not": None,
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
                    _configuration: typing.Optional[Configuration] = None,
                    **kwargs: typing.Type[Schema],
                ) -> "state":
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )

            @classmethod
            @property
            def taskDefinition(cls) -> typing.Type["TasksDefinitionSummary"]:
                return TasksDefinitionSummary

            processId = UUIDSchema
            activityToken = StrSchema
            activityResponseVersion = StrSchema

            class elementValues(DictSchema):
                def __new__(
                    cls,
                    *args: typing.Union[
                        dict,
                        frozendict,
                    ],
                    _configuration: typing.Optional[Configuration] = None,
                    **kwargs: typing.Type[Schema],
                ) -> "elementValues":
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )

            class logs(ListSchema):
                @classmethod
                @property
                def _items(cls) -> typing.Type["Log"]:
                    return Log

            class owner(ComposedSchema):
                @classmethod
                @property
                @functools.cache
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
                            Principal,
                        ],
                        "oneOf": [],
                        "anyOf": [],
                        "not": None,
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
                    _configuration: typing.Optional[Configuration] = None,
                    **kwargs: typing.Type[Schema],
                ) -> "owner":
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )

            def __new__(
                cls,
                *args: typing.Union[
                    dict,
                    frozendict,
                ],
                state: typing.Union[state, Unset] = unset,
                activityToken: typing.Union[activityToken, Unset] = unset,
                activityResponseVersion: typing.Union[
                    activityResponseVersion, Unset
                ] = unset,
                elementValues: typing.Union[elementValues, Unset] = unset,
                logs: typing.Union[logs, Unset] = unset,
                owner: typing.Union[owner, Unset] = unset,
                _configuration: typing.Optional[Configuration] = None,
                **kwargs: typing.Type[Schema],
            ) -> "allOf_1":
                return super().__new__(
                    cls,
                    *args,
                    state=state,
                    activityToken=activityToken,
                    activityResponseVersion=activityResponseVersion,
                    elementValues=elementValues,
                    logs=logs,
                    owner=owner,
                    _configuration=_configuration,
                    **kwargs,
                )

        return {
            "allOf": [
                AbstractAudited,
                allOf_1,
            ],
            "oneOf": [],
            "anyOf": [],
            "not": None,
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
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> "Task":
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )


from kuflow_rest_client.model.abstract_audited import AbstractAudited

# KF: Missing Imports
from kuflow_rest_client.model.task_state import TaskState
from kuflow_rest_client.model.tasks_definition_summary import TasksDefinitionSummary
from kuflow_rest_client.model.log import Log
from kuflow_rest_client.model.principal import Principal
# KF: END Missing Imports
