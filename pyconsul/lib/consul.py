from typing import List
from typing import Union

import httpx
from httpx import HTTPStatusError
from pydantic import Field
from pydantic.dataclasses import dataclass

from pyconsul.lib.exceptions import Unauthenticated
from pyconsul.lib.exceptions import UnknownResourceCalled


@dataclass
class ConsulAPI:
    address: str = Field(default="http://localhost:8500", env='CONSUL_HTTP_ADDR', description='Base address for Consul cluster/host.')
    token: str = Field(default=None, env='CONSUL_HTTP_TOKEN', description='Valid Consul token.')
    namespace: str = Field(default=None, env='CONSUL_NAMESPACE', description='Consul namespace to use for querying resources.')
    headers: dict = Field(default_factory=dict, description='Custom headers to include on each request.')

    def _get(self, endpoint: str) -> Union[dict, str, List[str]]:
        """
        Specifically making GET requests to Consul that expect JSON.

        Parameters
        ----------
        endpoint: str
            The specific endpoint to hit.

        Returns
        -------
        response: Union[dict, str, List[str]]

        Raises
        ------
        Unauthenticated
        UnknownResourceCalled
        """

        if self.token:
            self.headers.update(
                {
                    'X-Consul-Token': self.token
                }
            )

        params = {}
        if self.namespace:
            params = {'namespace': self.namespace}

        url = f'{self.address}/v1{endpoint}'
        try:

            response = httpx.get(url, headers=self.headers, params=params)

            response.raise_for_status()

        # Attempt to gracefully handle Consul's documented response codes with helpful exceptions
        except HTTPStatusError as http_error:
            if http_error.response.status_code == 403:
                raise Unauthenticated('API called failed to due being unauthenticated. Maybe your token expired?')
            if http_error.response.status_code == 404:
                raise UnknownResourceCalled('Received a 404. Check supported API endpoints for your version of Consul.')
            raise http_error

        return response.json()
