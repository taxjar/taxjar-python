import requests
import taxjar
from taxjar.response import TaxJarResponse
from taxjar.exceptions import TaxJarConnectionError

class Client(object):
    """TaxJar Python Client"""
    def __init__(self, api_key, options=None, responder=TaxJarResponse.from_request):
        if options is None:
            options = {}
        self.api_key = api_key
        self.timeout = options.get('timeout', 5)
        self.responder = responder

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

    def list_orders(self, params):
        """Lists existing order transactions."""
        request = self._get('transactions/orders', params)
        return self.responder(request)

    def show_order(self, order_id):
        """Shows an existing order transaction."""
        request = self._get('transactions/orders/' + str(order_id))
        return self.responder(request)

    def create_order(self, order_deets):
        """Creates a new order transaction."""
        request = self._post('transactions/orders', order_deets)
        return self.responder(request)

    def update_order(self, order_id, order_deets):
        """Updates an existing order transaction."""
        request = self._put("transactions/orders/" + str(order_id), order_deets)
        return self.responder(request)

    def delete_order(self, order_id):
        """Deletes an existing order transaction."""
        request = self._delete("transactions/orders/" + str(order_id))
        return self.responder(request)

    def list_refunds(self, params):
        """Lists existing refund transactions."""
        request = self._get('transactions/refunds', params)
        return self.responder(request)

    def show_refund(self, refund_id):
        """Shows an existing refund transaction."""
        request = self._get('transactions/refunds/' + str(refund_id))
        return self.responder(request)

    def create_refund(self, refund_deets):
        """Creates a new refund transaction."""
        request = self._post('transactions/refunds', refund_deets)
        return self.responder(request)

    def update_refund(self, refund_id, refund_deets):
        """Updates an existing refund transaction."""
        request = self._put('transactions/refunds/' + str(refund_id), refund_deets)
        return self.responder(request)

    def delete_refund(self, refund_id):
        """Deletes an existing refund transaction."""
        request = self._delete('transactions/refunds/' + str(refund_id))
        return self.responder(request)

    def nexus_regions(self):
        """Lists existing nexus locations for a TaxJar account."""
        request = self._get('nexus/regions')
        return self.responder(request)

    def validate(self, vat):
        """Validates an existing VAT identification number against VIES."""
        request = self._get('validation', {'vat': vat})
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

    def _delete(self, endpoint):
        return self._request(requests.delete, endpoint)

    def _request(self, method, endpoint, data=None):
        if data is None:
            data = {}
        try:
            data['timeout'] = self.timeout
            return method(self._uri(endpoint), headers=self._headers(), **data)
        except requests.Timeout as err:
            raise TaxJarConnectionError(err)
        except requests.ConnectionError as err:
            raise TaxJarConnectionError(err)

    @staticmethod
    def _uri(endpoint):
        return taxjar.API_URL + endpoint

    def _headers(self):
        return {'Authorization': 'Bearer ' + self.api_key,
                'User-Agent': 'TaxJarPython/' + taxjar.VERSION}
