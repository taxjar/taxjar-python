import platform
import ssl
import string
import sys
import requests
import taxjar
from taxjar.response import TaxJarResponse
from taxjar.exceptions import TaxJarConnectionError

class Client(object):
    """TaxJar Python Client"""
    def __init__(self, api_key, api_url="", options=None, responder=TaxJarResponse.from_request):
        if options is None:
            options = {}
        self.api_key = api_key
        self.api_url = api_url if api_url else taxjar.DEFAULT_API_URL
        self.api_url += "/" + taxjar.API_VERSION + "/"
        self.headers = options.get('headers', {})
        self.timeout = options.get('timeout', 5)
        self.responder = responder

    def set_api_config(self, key, value):
        if key is 'api_url':
            value += "/" + taxjar.API_VERSION + "/"
        setattr(self, key, value)

    def get_api_config(self, key):
        return getattr(self, key)

    def categories(self):
        """Lists all tax categories."""
        request = self._get('categories')
        return self.responder(request)

    def rates_for_location(self, postal_code, location_deets=None):
        """Shows the sales tax rates for a given location."""
        request = self._get("rates/" + postal_code, location_deets)
        return self.responder(request)

    def tax_for_order(self, order_deets):
        """Shows the sales tax that should be collected for a given order."""
        request = self._post('taxes', order_deets)
        return self.responder(request)

    def list_orders(self, params=None):
        """Lists existing order transactions."""
        request = self._get('transactions/orders', params)
        return self.responder(request)

    def show_order(self, order_id, params=None):
        """Shows an existing order transaction."""
        request = self._get('transactions/orders/' + str(order_id), params)
        return self.responder(request)

    def create_order(self, order_deets):
        """Creates a new order transaction."""
        request = self._post('transactions/orders', order_deets)
        return self.responder(request)

    def update_order(self, order_id, order_deets):
        """Updates an existing order transaction."""
        request = self._put("transactions/orders/" + str(order_id), order_deets)
        return self.responder(request)

    def delete_order(self, order_id, params=None):
        """Deletes an existing order transaction."""
        request = self._delete("transactions/orders/" + str(order_id), params)
        return self.responder(request)

    def list_refunds(self, params=None):
        """Lists existing refund transactions."""
        request = self._get('transactions/refunds', params)
        return self.responder(request)

    def show_refund(self, refund_id, params=None):
        """Shows an existing refund transaction."""
        request = self._get('transactions/refunds/' + str(refund_id), params)
        return self.responder(request)

    def create_refund(self, refund_deets):
        """Creates a new refund transaction."""
        request = self._post('transactions/refunds', refund_deets)
        return self.responder(request)

    def update_refund(self, refund_id, refund_deets):
        """Updates an existing refund transaction."""
        request = self._put('transactions/refunds/' + str(refund_id), refund_deets)
        return self.responder(request)

    def delete_refund(self, refund_id, params=None):
        """Deletes an existing refund transaction."""
        request = self._delete('transactions/refunds/' + str(refund_id), params)
        return self.responder(request)

    def list_customers(self, params=None):
        """Lists existing customers."""
        request = self._get('customers', params)
        return self.responder(request)

    def show_customer(self, customer_id):
        """Shows an existing customer."""
        request = self._get('customers/' + str(customer_id))
        return self.responder(request)

    def create_customer(self, customer_deets):
        """Creates a new customer."""
        request = self._post('customers', customer_deets)
        return self.responder(request)

    def update_customer(self, customer_id, customer_deets):
        """Updates an existing customer."""
        request = self._put("customers/" + str(customer_id), customer_deets)
        return self.responder(request)

    def delete_customer(self, customer_id):
        """Deletes an existing customer."""
        request = self._delete("customers/" + str(customer_id))
        return self.responder(request)

    def nexus_regions(self):
        """Lists existing nexus locations for a TaxJar account."""
        request = self._get('nexus/regions')
        return self.responder(request)

    def validate_address(self, address_deets):
        """Validates a customer address and returns back a collection of address matches."""
        request = self._post('addresses/validate', address_deets)
        return self.responder(request)

    def validate(self, vat_deets):
        """Validates an existing VAT identification number against VIES."""
        request = self._get('validation', vat_deets)
        return self.responder(request)

    def summary_rates(self):
        """Retrieve minimum and average sales tax rates by region as a backup."""
        request = self._get('summary_rates')
        return self.responder(request)

    def _get(self, endpoint, data=None):
        if data is None:
            data = {}
        return self._request(requests.get, endpoint, {'params': data})

    def _post(self, endpoint, data):
        return self._request(requests.post, endpoint, {'json': data})

    def _put(self, endpoint, data):
        return self._request(requests.put, endpoint, {'json': data})

    def _delete(self, endpoint, data=None):
        if data is None:
            data = {}
        return self._request(requests.delete, endpoint, {'params': data})

    def _request(self, method, endpoint, data=None):
        if data is None:
            data = {}
        try:
            data['timeout'] = self.timeout
            return method(self._uri(self.api_url, endpoint), headers=self._headers(), **data)
        except requests.Timeout as err:
            raise TaxJarConnectionError(err)
        except requests.ConnectionError as err:
            raise TaxJarConnectionError(err)

    @staticmethod
    def _uri(api_url, endpoint):
        return api_url + endpoint

    @staticmethod
    def _get_user_agent():
        platform_str = ' '.join(platform.uname())
        python_version = '.'.join((str(i) for i in sys.version_info[0:3]))
        try:
            open_ssl_version = ssl.OPENSSL_VERSION
        except AttributeError:
            open_ssl_version = ''
        return 'TaxJar/Python (%s; python %s; %s) taxjar-python/%s' % (platform_str, python_version, open_ssl_version, taxjar.VERSION)

    def _default_headers(self):
        return {'Authorization': 'Bearer ' + self.api_key,
                'User-Agent': self._get_user_agent()}

    def _headers(self):
        headers = self._default_headers().copy()
        headers.update(self.headers)
        return headers
