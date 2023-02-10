import unittest

from hc_pyconsul.helpers.services import extract_alloc_id_from_service_name


class TestHelpersExtractAllocationID(unittest.TestCase):
    def test_extract_alloc_id(self):
        results = extract_alloc_id_from_service_name(
            service_id='_nomad-task-86c6736f-33d2-e3b1-69a2-8189031eb599-service-01'
        )

        assert results.id == '86c6736f'
        assert results.id_long == '86c6736f-33d2-e3b1-69a2-8189031eb599'

    def test_extract_alloc_id_unknown_pattern(self):
        results = extract_alloc_id_from_service_name(
            service_id='86c6736f-33d2-e3b1-69a2-8189031eb599'
        )

        assert results.id == ''
        assert results.id_long == ''
