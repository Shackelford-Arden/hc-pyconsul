import pytest
import respx

from hc_pyconsul.lib.consul import ConsulAPI
from hc_pyconsul.lib.exceptions import Unauthenticated


@respx.mock
def test_get_403(respx_mock):
    nomad = ConsulAPI()
    endpoint = '/testing403'
    mocked_route = respx_mock.get(url=f'{nomad.address}/v1{endpoint}')
    mocked_route.respond(status_code=403, json={})

    with pytest.raises(Unauthenticated):
        nomad._get(endpoint=endpoint)
