import unittest
from unittest.mock import MagicMock, patch
from taxjar.exceptions import TaxJarResponseError
from taxjar.factory import TaxJarTypeFactory
from taxjar.response import TaxJarResponse

class TestTaxJarFactory(unittest.TestCase):
    def setUp(self):
        self.response_data = {}
        self.request = MagicMock()

    def test_data_from_successful_request(self):
        self.request.status_code = 200
        self.request.json = MagicMock(return_value = { 'type': 'value' })
        with patch.object(TaxJarTypeFactory, 'build') as factory_mock:
            TaxJarResponse().data_from_request(self.request)
            factory_mock.called_with('type').return_value.called_with('value')

    def test_data_from_failed_request(self):
        self.request.status_code = 500
        self.request.json = MagicMock(return_value = { 'status': 500, 'error': 'Server Error', 'detail': 'some detail' })
        try:
            TaxJarResponse().data_from_request(self.request)
        except TaxJarResponseError as e:
            self.assertEqual(str(e), "500 Server Error")
            self.assertEqual(e.full_response['detail'], 'some detail')
            self.assertEqual(e.full_response['response'], self.request.json())
