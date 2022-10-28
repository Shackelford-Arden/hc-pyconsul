from unittest import TestCase

import respx
from httpx import Response

from hc_pyconsul import ConsulCatalog


class TestListServices(TestCase):

    def setUp(self) -> None:
        self.test_catalog = ConsulCatalog()

    def tearDown(self) -> None:
        self.test_catalog = None

    @respx.mock
    def test_valid_services_call(self):
        call_response = {
            "consul": [],
            "redis": [],
            "postgresql": ["primary", "secondary"]
        }

        response = respx.get('http://localhost:8500/v1/catalog/services')
        response.return_value = Response(200, json=call_response)

        services = self.test_catalog.list_services()

        assert isinstance(services['redis'], list)
        self.assertEqual(len(services['consul']), 0)
