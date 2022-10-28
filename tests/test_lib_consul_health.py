from unittest import TestCase

import pytest
import respx
from httpx import Response

from hc_pyconsul import ConsulHealth
from hc_pyconsul.exceptions import Unauthenticated
from hc_pyconsul.lib.consul import ConsulAPI
from hc_pyconsul.models.health import ServiceHealth
from tests.fixtures.health import responses


@respx.mock
def test_get_403(respx_mock):
    nomad = ConsulAPI()
    endpoint = '/testing403'
    mocked_route = respx_mock.get(url=f'{nomad.address}/v1{endpoint}')
    mocked_route.respond(status_code=403, json={})

    with pytest.raises(Unauthenticated):
        nomad.call_api(endpoint=endpoint, verb='GET')


class TestListServiceInstances(TestCase):

    def setUp(self) -> None:
        self.test_health = ConsulHealth()

    def tearDown(self) -> None:
        self.test_health = None

    @respx.mock
    def test_valid_response(self):
        response = respx.get('http://localhost:8500/v1/health/service/foobar')
        response.return_value = Response(200, json=responses.HEALTH_SERVICES_LIST)

        services: list[ServiceHealth] = self.test_health.list_service_instances(service='foobar')

        self.assertEqual(services[0].service.id, 'redis')
