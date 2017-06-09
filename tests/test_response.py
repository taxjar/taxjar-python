import unittest
from mock import MagicMock, patch
from taxjar.exceptions import TaxJarResponseError
from taxjar.factory import TaxJarTypeFactory
from taxjar.response import TaxJarResponse

class TestTaxJarFactory(unittest.TestCase):
    def setUp(self):
        self.response_data = {}
        self.request = MagicMock()

    def test_data_from_successful_request(self):
        self.request.status_code = 200
        self.request.json = MagicMock(return_value={'type': 'value'})
        with patch.object(TaxJarTypeFactory, 'build') as factory_mock:
            TaxJarResponse().data_from_request(self.request)
            factory_mock.called_with('type').return_value.called_with('value')

    def test_data_from_failed_400_request(self):
        self.request.status_code = 400
        self.request.json = MagicMock(return_value={
            'status': 400,
            'error': 'Bad Request',
            'detail': 'some detail'
        })
        try:
            TaxJarResponse().data_from_request(self.request)
            self.assertTrue(False)
        except TaxJarResponseError as err:
            self.assertEqual(str(err), "400 Bad Request")
            self.assertEqual(err.full_response['detail'], 'some detail')
            self.assertEqual(err.full_response['response'], self.request.json())

    def test_data_from_failed_500_request(self):
        self.request.status_code = 500
        self.request.json = MagicMock(return_value={
            'status': 500,
            'error': 'Server Error',
            'detail': 'some detail'
        })
        try:
            TaxJarResponse().data_from_request(self.request)
            self.assertTrue(False)
        except TaxJarResponseError as err:
            self.assertEqual(str(err), "500 Server Error")
            self.assertEqual(err.full_response['detail'], 'some detail')
            self.assertEqual(err.full_response['response'], self.request.json())
