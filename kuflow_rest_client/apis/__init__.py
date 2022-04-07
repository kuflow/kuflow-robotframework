# coding: utf-8

# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.authentication_api import AuthenticationApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from kuflow_rest_client.api.authentication_api import AuthenticationApi
from kuflow_rest_client.api.process_api import ProcessApi
from kuflow_rest_client.api.task_api import TaskApi
