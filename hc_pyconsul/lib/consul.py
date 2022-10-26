import os
from typing import Optional

import httpx
from httpx import HTTPStatusError
from pydantic.dataclasses import dataclass

from hc_pyconsul.lib.exceptions import Unauthenticated
from hc_pyconsul.lib.exceptions import UnknownResourceCalled


@dataclass
class ConsulAPI:
    address: str = "http://localhost:8500"
    token: Optional[str] = None
    namespace: Optional[str] = None

    def __post_init__(self):

        if os.environ.get('CONSUL_HTTP_ADDR'):
            self.address = os.environ.get('CONSUL_HTTP_ADDR')

        if os.environ.get('CONSUL_HTTP_TOKEN'):
            self.token = os.environ.get('CONSUL_HTTP_TOKEN')

        if os.environ.get('CONSUL_NAMESPACE'):
            self.namespace = os.environ.get('CONSUL_NAMESPACE')

    def _get(self, endpoint: str, **kwargs):
        """
        Specifically making GET requests to Consul that expect JSON.

        Parameters
        ----------
        endpoint: str
            The specific endpoint to hit.

        Returns
        -------
        response

        Raises
        ------
        Unauthenticated
        UnknownResourceCalled
        """

        call_headers = kwargs.get('headers', {})

        if self.token:
            call_headers.update(
                {
                    'X-Consul-Token': self.token
                }
            )

        if self.namespace:
            if not kwargs.get('params'):
                kwargs['params'] = {}

            kwargs['params'].update({'namespace': self.namespace})

        url = f'{self.address}/v1{endpoint}'
        try:

            response = httpx.get(url, headers=call_headers, **kwargs)

            response.raise_for_status()

        # Attempt to gracefully handle Consul's documented response codes with helpful exceptions
        except HTTPStatusError as http_error:
            if http_error.response.status_code == 403:
                raise Unauthenticated('API called failed to due being unauthenticated. Maybe your token expired?')
            if http_error.response.status_code == 404:
                raise UnknownResourceCalled('Received a 404. Check supported API endpoints for your version of Consul.')
            raise http_error

        return response.json()
