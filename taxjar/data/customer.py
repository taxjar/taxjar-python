from jsonobject import JsonObject, StringProperty, ListProperty
from taxjar.data.exempt_region import TaxJarExemptRegion
from taxjar.data.iterable import TaxJarIterable

class TaxJarCustomer(JsonObject):
    customer_id = StringProperty()
    exemption_type = StringProperty()
    name = StringProperty()
    country = StringProperty()
    state = StringProperty()
    zip = StringProperty()
    city = StringProperty()
    street = StringProperty()

    exempt_regions = ListProperty(TaxJarExemptRegion)

class TaxJarCustomers(TaxJarIterable):
    def handle_response(self, response):
        self.data = response
        return self
