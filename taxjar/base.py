import requests
from taxjar.response import TaxJarResponse

class TaxJar:
    API_URL = "http://taxjar.dev:3002/v2/"
    API_KEY = "4761b5420b86988ca376712b20f743cb"

    def rates_for_location(self, postal_code):
        request = self._get("rates/" + postal_code)
        return TaxJarResponse().from_request(request)

    def categories(self):
        request = self._get('categories')
        return TaxJarResponse().from_request(request)

    def tax_for_order(self, order_deets):
        request = self._post('taxes', order_deets)
        return TaxJarResponse().from_request(request)

    def list_orders(self, params):
        request = self._get('transactions/orders', params)
        return TaxJarResponse().from_request(request)

    def show_order(self, order_id):
        request = self._get('transactions/orders/' + str(order_id))
        return TaxJarResponse().from_request(request)

    def create_order(self, order_deets):
        request = self._post('transactions/orders', order_deets)
        return TaxJarResponse().from_request(request)

    def update_order(self, order_id, order_deets):
        request = self._put("transactions/orders/" + str(order_id), order_deets)
        return TaxJarResponse().from_request(request)

    def delete_order(self, order_id):
        request = self._delete("transactions/orders/" + str(order_id))
        return TaxJarResponse().from_request(request)

    def list_refunds(self, params):
        request = self._get('transactions/refunds', params)
        return TaxJarResponse().from_request(request)

    def show_refund(self, refund_id):
        request = self._get('transactions/refunds/' + str(refund_id))
        return TaxJarResponse().from_request(request)

    def create_refund(self, refund_deets):
        request = self._post('transactions/refunds', refund_deets)
        return TaxJarResponse().from_request(request)

    def update_refund(self, refund_id, refund_deets):
        request = self._put("transactions/refunds/" + str(refund_id), refund_deets)
        return TaxJarResponse().from_request(request)

    def delete_refund(self, refund_id):
        request = self._delete("transactions/refunds/" + str(refund_id))
        return TaxJarResponse().from_request(request)

    def nexus_regions(self):
        request = self._get("nexus/regions")
        return TaxJarResponse().from_request(request)

    def validate(self, vat):
        request = self._get("validation", { "vat": vat })
        return TaxJarResponse().from_request(request)

    def summary_rates(self):
        request = self._get("summary_rates")
        return TaxJarResponse().from_request(request)

    def _headers(self):
        return { "Authorization": "Bearer " + self.API_KEY }

    def _get(self, endpoint, extra_data = {}):
        return requests.get(self.uri(endpoint), headers = self._headers(), params = extra_data)

    def _post(self, endpoint, data):
        return requests.post(self.uri(endpoint), headers = self._headers(), json = data)

    def _put(self, endpoint, data):
        return requests.put(self.uri(endpoint), headers = self._headers(), json = data)

    def _delete(self, endpoint):
        return requests.delete(self.uri(endpoint), headers = self._headers())

    def uri(self, endpoint):
        return self.API_URL + endpoint
