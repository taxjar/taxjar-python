import requests
from taxjar.response import TaxJarResponse
from taxjar.exceptions import TaxJarConnectionError

class TaxJarClient:
    API_URL = "http://taxjar.dev:3002/v2/"
    VERSION = '0.0.1'

    def __init__(self, key, options = {}, responder = TaxJarResponse.from_request):
        self.api_key = key
        self.timeout = options.get('timeout', 5)
        self.responder = responder

    def rates_for_location(self, postal_code):
        request = self._get("rates/" + postal_code)
        return self.responder(request)

    def categories(self):
        request = self._get('categories')
        return self.responder(request)

    def tax_for_order(self, order_deets):
        request = self._post('taxes', order_deets)
        return self.responder(request)

    def list_orders(self, params):
        request = self._get('transactions/orders', params)
        return self.responder(request)

    def show_order(self, order_id):
        request = self._get('transactions/orders/' + str(order_id))
        return self.responder(request)

    def create_order(self, order_deets):
        request = self._post('transactions/orders', order_deets)
        return self.responder(request)

    def update_order(self, order_id, order_deets):
        request = self._put("transactions/orders/" + str(order_id), order_deets)
        return self.responder(request)

    def delete_order(self, order_id):
        request = self._delete("transactions/orders/" + str(order_id))
        return self.responder(request)

    def list_refunds(self, params):
        request = self._get('transactions/refunds', params)
        return self.responder(request)

    def show_refund(self, refund_id):
        request = self._get('transactions/refunds/' + str(refund_id))
        return self.responder(request)

    def create_refund(self, refund_deets):
        request = self._post('transactions/refunds', refund_deets)
        return self.responder(request)

    def update_refund(self, refund_id, refund_deets):
        request = self._put("transactions/refunds/" + str(refund_id), refund_deets)
        return self.responder(request)

    def delete_refund(self, refund_id):
        request = self._delete("transactions/refunds/" + str(refund_id))
        return self.responder(request)

    def nexus_regions(self):
        request = self._get("nexus/regions")
        return self.responder(request)

    def validate(self, vat):
        request = self._get("validation", { "vat": vat })
        return self.responder(request)

    def summary_rates(self):
        request = self._get("summary_rates")
        return self.responder(request)

    def _get(self, endpoint, data = {}):
        return self._request(requests.get, endpoint, { 'params': data })

    def _post(self, endpoint, data):
        return self._request(requests.post, endpoint, { 'json': data })

    def _put(self, endpoint, data):
        return self._request(requests.put, endpoint, { 'json': data })

    def _delete(self, endpoint):
        return self._request(requests.delete, endpoint)

    def _request(self, method, endpoint, data = {}):
        try:
            data['timeout'] = self.timeout
            return method(self._uri(endpoint), headers = self._headers(), **data)
        except requests.Timeout as e:
            raise TaxJarConnectionError(e)
        except requests.ConnectionError as e:
            raise TaxJarConnectionError(e)

    def _uri(self, endpoint):
        return self.API_URL + endpoint

    def _headers(self):
        return { "Authorization": "Bearer " + self.api_key, "User-Agent": "TaxJarPython/" + self.VERSION }
