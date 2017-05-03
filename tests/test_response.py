import unittest
from mock import MagicMock, patch
from taxjar.exceptions import ResponseError
from taxjar.factory import TypeFactory
from taxjar.response import Response

class TestTaxJarFactory(unittest.TestCase):
    def setUp(self):
        self.response_data = {}
        self.request = MagicMock()

    def test_data_from_successful_request(self):
        self.request.status_code = 200
        self.request.json = MagicMock(return_value = {'type': 'value'})
        with patch.object(TypeFactory, 'build') as factory_mock:
            Response().data_from_request(self.request)
            factory_mock.called_with('type').return_value.called_with('value')

    def test_data_from_failed_request(self):
        self.request.status_code = 500
        self.request.json = MagicMock(return_value = {'status': 500, 'error': 'Server Error', 'detail': 'some detail'})
        try:
            Response().data_from_request(self.request)
            self.assertTrue(False)
        except ResponseError as e:
            self.assertEqual(str(e), "500 Server Error")
            self.assertEqual(e.full_response['detail'], 'some detail')
            self.assertEqual(e.full_response['response'], self.request.json())
