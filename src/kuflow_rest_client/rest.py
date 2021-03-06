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

import logging
import ssl
from urllib.parse import urlencode
import typing

import certifi
import urllib3
from urllib3._collections import HTTPHeaderDict

from kuflow_rest_client.exceptions import ApiException, ApiValueError


logger = logging.getLogger(__name__)


class RESTClientObject(object):
    def __init__(self, configuration, pools_size=4, maxsize=None):
        # urllib3.PoolManager will pass all kw parameters to connectionpool
        # https://github.com/shazow/urllib3/blob/f9409436f83aeb79fbaf090181cd81b784f1b8ce/urllib3/poolmanager.py#L75  # noqa: E501
        # https://github.com/shazow/urllib3/blob/f9409436f83aeb79fbaf090181cd81b784f1b8ce/urllib3/connectionpool.py#L680  # noqa: E501
        # maxsize is the number of requests to host that are allowed in parallel  # noqa: E501
        # Custom SSL certificates and client certificates: http://urllib3.readthedocs.io/en/latest/advanced-usage.html  # noqa: E501

        # cert_reqs
        if configuration.verify_ssl:
            cert_reqs = ssl.CERT_REQUIRED
        else:
            cert_reqs = ssl.CERT_NONE

        # ca_certs
        if configuration.ssl_ca_cert:
            ca_certs = configuration.ssl_ca_cert
        else:
            # if not set certificate file, use Mozilla's root certificates.
            ca_certs = certifi.where()

        addition_pool_args = {}
        if configuration.assert_hostname is not None:
            addition_pool_args[
                "assert_hostname"
            ] = configuration.assert_hostname  # noqa: E501

        if configuration.retries is not None:
            addition_pool_args["retries"] = configuration.retries

        if configuration.socket_options is not None:
            addition_pool_args["socket_options"] = configuration.socket_options

        if maxsize is None:
            if configuration.connection_pool_maxsize is not None:
                maxsize = configuration.connection_pool_maxsize
            else:
                maxsize = 4

        # https pool manager
        if configuration.proxy:
            self.pool_manager = urllib3.ProxyManager(
                num_pools=pools_size,
                maxsize=maxsize,
                cert_reqs=cert_reqs,
                ca_certs=ca_certs,
                cert_file=configuration.cert_file,
                key_file=configuration.key_file,
                proxy_url=configuration.proxy,
                proxy_headers=configuration.proxy_headers,
                **addition_pool_args,
            )
        else:
            self.pool_manager = urllib3.PoolManager(
                num_pools=pools_size,
                maxsize=maxsize,
                cert_reqs=cert_reqs,
                ca_certs=ca_certs,
                cert_file=configuration.cert_file,
                key_file=configuration.key_file,
                **addition_pool_args,
            )

    def request(
        self,
        method: str,
        url: str,
        query_params: typing.Optional[typing.Tuple[typing.Tuple[str, str], ...]] = None,
        headers: typing.Optional[HTTPHeaderDict] = None,
        fields: typing.Optional[
            typing.Tuple[typing.Tuple[str, typing.Any], ...]
        ] = None,
        body: typing.Optional[typing.Union[str, bytes]] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> urllib3.HTTPResponse:
        """Perform requests.

        :param method: http request method
        :param url: http request url
        :param query_params: query parameters in the url
        :param headers: http request headers
        :param body: request body, for other types
        :param fields: request parameters for
                                `application/x-www-form-urlencoded`
                                or `multipart/form-data`
        :param stream: if True, the urllib3.HTTPResponse object will
                                be returned without reading/decoding response
                                data. Default is False.
        :param timeout: timeout setting for this request. If one
                                number provided, it will be total request
                                timeout. It can also be a pair (tuple) of
                                (connection, read) timeouts.
        """
        method = method.upper()
        assert method in ["GET", "HEAD", "DELETE", "POST", "PUT", "PATCH", "OPTIONS"]

        if fields and body:
            raise ApiValueError("body parameter cannot be used with fields parameter.")

        fields = fields or {}
        headers = headers or {}

        if timeout:
            if isinstance(timeout, (int, float)):  # noqa: E501,F821
                timeout = urllib3.Timeout(total=timeout)
            elif isinstance(timeout, tuple) and len(timeout) == 2:
                timeout = urllib3.Timeout(connect=timeout[0], read=timeout[1])

        try:
            # For `POST`, `PUT`, `PATCH`, `OPTIONS`, `DELETE`
            if method in ["POST", "PUT", "PATCH", "OPTIONS", "DELETE"]:
                if query_params:
                    url += "?" + urlencode(query_params)
                if "Content-Type" not in headers and body is None:
                    r = self.pool_manager.request(
                        method,
                        url,
                        fields=query_params,
                        preload_content=not stream,
                        timeout=timeout,
                        headers=headers,
                    )
                elif (
                    headers["Content-Type"] == "application/x-www-form-urlencoded"
                ):  # noqa: E501
                    r = self.pool_manager.request(
                        method,
                        url,
                        fields=fields,
                        encode_multipart=False,
                        preload_content=not stream,
                        timeout=timeout,
                        headers=headers,
                    )
                elif headers["Content-Type"] == "multipart/form-data":
                    # must del headers['Content-Type'], or the correct
                    # Content-Type which generated by urllib3 will be
                    # overwritten.
                    del headers["Content-Type"]
                    r = self.pool_manager.request(
                        method,
                        url,
                        fields=fields,
                        encode_multipart=True,
                        preload_content=not stream,
                        timeout=timeout,
                        headers=headers,
                    )
                # Pass a `string` parameter directly in the body to support
                # other content types than Json when `body` argument is
                # provided in serialized form
                elif isinstance(body, str) or isinstance(body, bytes):
                    request_body = body
                    r = self.pool_manager.request(
                        method,
                        url,
                        body=request_body,
                        preload_content=not stream,
                        timeout=timeout,
                        headers=headers,
                    )
                else:
                    # Cannot generate the request from given parameters
                    msg = """Cannot prepare a request message for provided
                             arguments. Please check that your arguments match
                             declared content type."""
                    raise ApiException(status=0, reason=msg)
            # For `GET`, `HEAD`
            else:
                r = self.pool_manager.request(
                    method,
                    url,
                    fields=query_params,
                    preload_content=not stream,
                    timeout=timeout,
                    headers=headers,
                )
        except urllib3.exceptions.SSLError as e:
            msg = "{0}\n{1}".format(type(e).__name__, str(e))
            raise ApiException(status=0, reason=msg)

        if not stream:
            # log response body
            logger.debug("response body: %s", r.data)

        return r

    def GET(
        self,
        url,
        headers=None,
        query_params=None,
        stream=False,
        timeout=None,
        fields=None,
    ) -> urllib3.HTTPResponse:
        return self.request(
            "GET",
            url,
            headers=headers,
            stream=stream,
            timeout=timeout,
            query_params=query_params,
            fields=fields,
        )

    def HEAD(
        self,
        url,
        headers=None,
        query_params=None,
        stream=False,
        timeout=None,
        fields=None,
    ) -> urllib3.HTTPResponse:
        return self.request(
            "HEAD",
            url,
            headers=headers,
            stream=stream,
            timeout=timeout,
            query_params=query_params,
            fields=fields,
        )

    def OPTIONS(
        self,
        url,
        headers=None,
        query_params=None,
        body=None,
        stream=False,
        timeout=None,
        fields=None,
    ) -> urllib3.HTTPResponse:
        return self.request(
            "OPTIONS",
            url,
            headers=headers,
            query_params=query_params,
            stream=stream,
            timeout=timeout,
            body=body,
            fields=fields,
        )

    def DELETE(
        self,
        url,
        headers=None,
        query_params=None,
        body=None,
        stream=False,
        timeout=None,
        fields=None,
    ) -> urllib3.HTTPResponse:
        return self.request(
            "DELETE",
            url,
            headers=headers,
            query_params=query_params,
            stream=stream,
            timeout=timeout,
            body=body,
            fields=fields,
        )

    def POST(
        self,
        url,
        headers=None,
        query_params=None,
        body=None,
        stream=False,
        timeout=None,
        fields=None,
    ) -> urllib3.HTTPResponse:
        return self.request(
            "POST",
            url,
            headers=headers,
            query_params=query_params,
            stream=stream,
            timeout=timeout,
            body=body,
            fields=fields,
        )

    def PUT(
        self,
        url,
        headers=None,
        query_params=None,
        body=None,
        stream=False,
        timeout=None,
        fields=None,
    ) -> urllib3.HTTPResponse:
        return self.request(
            "PUT",
            url,
            headers=headers,
            query_params=query_params,
            stream=stream,
            timeout=timeout,
            body=body,
            fields=fields,
        )

    def PATCH(
        self,
        url,
        headers=None,
        query_params=None,
        body=None,
        stream=False,
        timeout=None,
        fields=None,
    ) -> urllib3.HTTPResponse:
        return self.request(
            "PATCH",
            url,
            headers=headers,
            query_params=query_params,
            stream=stream,
            timeout=timeout,
            body=body,
            fields=fields,
        )
