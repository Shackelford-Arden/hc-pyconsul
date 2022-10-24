from typing import List

from pydantic.dataclasses import dataclass

from hc_pyconsul.lib.consul import ConsulAPI


@dataclass
class ConsulCatalog(ConsulAPI):

    def list_services(self, dc: str = None, node_meta: List[str] = None):
        """
        Link to official docs:
            https://developer.hashicorp.com/consul/api-docs/catalog#list-services

        Returns
        -------

        """
