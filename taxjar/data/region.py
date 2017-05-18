from jsonobject import JsonObject, StringProperty
from taxjar.data.iterable import TaxJarIterable

class TaxJarRegion(JsonObject):
    country_code = StringProperty()
    country = StringProperty()
    region_code = StringProperty()
    region = StringProperty()

class TaxJarRegions(TaxJarIterable):
    def handle_response(self, response):
        self.data = [TaxJarRegion(r) for r in response]
        return self
