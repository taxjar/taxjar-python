import re
from mock import MagicMock, patch
import requests
import unittest
import taxjar
import sys

class TestClient(unittest.TestCase):
    def setUp(self):
        self.api_key = 'heythere'
        self.api_url = taxjar.DEFAULT_API_URL + "/" + taxjar.API_VERSION + "/"
        self.headers = {"Authorization": "Bearer heythere"}
        self.responder_mock = MagicMock()
        self.client = taxjar.Client(api_key=self.api_key, options={}, responder=self.responder_mock)

    def test_client_params(self):
        self.client = taxjar.Client(api_key=self.api_key, api_url='https://api.sandbox.taxjar.com', options={
            'headers': {
                'X-TJ-Expected-Response': '422'
            }
        }, responder=self.responder_mock)
        self.assertEqual(self.client.api_url, 'https://api.sandbox.taxjar.com/v2/')
        self.assertEqual(self.client.headers, { 'X-TJ-Expected-Response': '422' })

    def test_set_api_config(self):
        self.client.set_api_config('api_url', 'https://api.sandbox.taxjar.com')
        self.assertEqual(self.client.api_url, 'https://api.sandbox.taxjar.com/v2/')

    def test_get_api_config(self):
        self.client.set_api_config('api_url', 'https://api.sandbox.taxjar.com')
        self.assertEqual(self.client.get_api_config('api_url'), self.client.api_url)

    def test_custom_headers(self):
        self.client.set_api_config('headers', {
            'X-TJ-Expected-Response': '422'
        })
        self.assertEqual(self.client.headers, {
            'X-TJ-Expected-Response': '422'
        })
        self.assertEqual(self.client._headers()['X-TJ-Expected-Response'], '422')
        self.assertEqual(self.client._headers()['Authorization'], 'Bearer heythere')
        self._assertRegexp(self.client._headers()['User-Agent'], re.compile('TaxJar/Python \\(.+\\) taxjar-python/\\d+\\.\\d+\\.\\d+'))

    def test_rates_for_location(self):
        action = lambda _: self.client.rates_for_location('90210')
        self.assert_request_occurred(action, 'get', 'rates/90210', {})

    def test_rates_for_location_with_deets(self):
        action = lambda _: self.client.rates_for_location('90210', {
            'city': 'Beverly Hills',
            'country': 'US'
        })
        self.assert_request_occurred(action, 'get', 'rates/90210', {
            'city': 'Beverly Hills',
            'country': 'US'
        })

    def test_categories(self):
        action = lambda _: self.client.categories()
        self.assert_request_occurred(action, 'get', 'categories', {})

    def test_tax_for_order(self):
        data = {'shipping': 0}
        action = lambda _: self.client.tax_for_order(data)
        self.assert_request_occurred(action, 'post', 'taxes', data)

    def test_list_orders(self):
        data = {'dummy': 'data'}
        action = lambda _: self.client.list_orders(data)
        self.assert_request_occurred(action, 'get', 'transactions/orders', data)
        action = lambda _: self.client.list_orders()
        self.assert_request_occurred(action, 'get', 'transactions/orders', {})

    def test_show_order(self):
        action = lambda _: self.client.show_order('1001')
        self.assert_request_occurred(action, 'get', 'transactions/orders/1001', {})
        action = lambda _: self.client.show_order('1001', {'provider': 'api'})
        self.assert_request_occurred(action, 'get', 'transactions/orders/1001', {
            'provider': 'api'
        })

    def test_create_order(self):
        data = {'dummy': 'data'}
        action = lambda _: self.client.create_order(data)
        self.assert_request_occurred(action, 'post', 'transactions/orders', data)

    def test_update_order(self):
        data = {'dummy': 'data'}
        action = lambda _: self.client.update_order(1, data)
        self.assert_request_occurred(action, 'put', 'transactions/orders/1', data)

    def test_delete_order(self):
        action = lambda _: self.client.delete_order(1)
        self.assert_request_occurred(action, 'delete', 'transactions/orders/1', {})
        action = lambda _: self.client.delete_order(1, {'provider': 'api'})
        self.assert_request_occurred(action, 'delete', 'transactions/orders/1', {
            'provider': 'api'
        })

    def test_list_refunds(self):
        data = {'from_transaction_date': '2016/01/01', 'to_transaction_date': '2017/01/01'}
        action = lambda _: self.client.list_refunds(data)
        self.assert_request_occurred(action, 'get', 'transactions/refunds', data)
        action = lambda _: self.client.list_refunds()
        self.assert_request_occurred(action, 'get', 'transactions/refunds', {})

    def test_show_refund(self):
        action = lambda _: self.client.show_refund('1001')
        self.assert_request_occurred(action, 'get', 'transactions/refunds/1001', {})
        action = lambda _: self.client.show_refund('1001', {'provider': 'api'})
        self.assert_request_occurred(action, 'get', 'transactions/refunds/1001', {
            'provider': 'api'
        })

    def test_create_refund(self):
        data = {'dummy': 'data'}
        action = lambda _: self.client.create_refund(data)
        self.assert_request_occurred(action, 'post', 'transactions/refunds', data)

    def test_update_refund(self):
        data = {'dummy': 'data'}
        action = lambda _: self.client.update_refund(1, data)
        self.assert_request_occurred(action, 'put', 'transactions/refunds/1', data)

    def test_delete_refund(self):
        action = lambda _: self.client.delete_refund(1)
        self.assert_request_occurred(action, 'delete', 'transactions/refunds/1', {})
        action = lambda _: self.client.delete_refund(1, {'provider': 'api'})
        self.assert_request_occurred(action, 'delete', 'transactions/refunds/1', {
            'provider': 'api'
        })

    def test_list_customers(self):
        action = lambda _: self.client.list_customers()
        self.assert_request_occurred(action, 'get', 'customers', {})

    def test_show_customer(self):
        action = lambda _: self.client.show_customer('123')
        self.assert_request_occurred(action, 'get', 'customers/123', {})

    def test_create_customer(self):
        data = {'dummy': 'data'}
        action = lambda _: self.client.create_customer(data)
        self.assert_request_occurred(action, 'post', 'customers', data)

    def test_update_customer(self):
        data = {'dummy': 'data'}
        action = lambda _: self.client.update_customer('123', data)
        self.assert_request_occurred(action, 'put', 'customers/123', data)

    def test_delete_customer(self):
        action = lambda _: self.client.delete_customer('123')
        self.assert_request_occurred(action, 'delete', 'customers/123', {})

    def test_nexus_regions(self):
        action = lambda _: self.client.nexus_regions()
        self.assert_request_occurred(action, 'get', 'nexus/regions', {})

    def test_validate_address(self):
        data = {'country': 'US', 'state': 'AZ', 'zip': '85297', 'city': 'Gilbert', 'street': '3301 South Greenfield Rd'}
        action = lambda _: self.client.validate_address(data)
        self.assert_request_occurred(action, 'post', 'addresses/validate', data)

    def test_validate(self):
        action = lambda _: self.client.validate({'vat': '1234'})
        self.assert_request_occurred(action, 'get', 'validation', {'vat': '1234'})

    def test_summary_rates(self):
        action = lambda _: self.client.summary_rates()
        self.assert_request_occurred(action, 'get', 'summary_rates', {})

    def assert_request_occurred(self, action, request_method, uri, params):
        url = self.api_url + uri
        with patch.object(requests.Session, request_method) as request_mock:
            action(0)
            request_mock.assert_called_with(
                url,
                headers=self.client._headers(),
                **self._request_args(request_method, params)
            )
            self.responder_mock.assert_called_with(request_mock.return_value)

    def _request_args(self, method, params):
        args = {'timeout': 5}
        if method == 'get' or method == 'delete':
            args['params'] = params
        else:
            args['json'] = params
        return args

    def _assertRegexp(self, a, b):
        if sys.version_info >= (3,2):
            return self.assertRegex(a, b)
        else:
            return self.assertRegexpMatches(a, b)
