from jsonobject import JsonObject, StringProperty
from taxjar.data.iterable import TaxJarIterable

class TaxJarAddress(JsonObject):
    country = StringProperty()
    state = StringProperty()
    zip = StringProperty()
    city = StringProperty()
    street = StringProperty()

class TaxJarAddresses(TaxJarIterable):
    def handle_response(self, response):
        self.data = [TaxJarAddress(r) for r in response]
        return self
