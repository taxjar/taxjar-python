from jsonobject import JsonObject, StringProperty
from taxjar.data.iterable import TaxJarIterable

class TaxJarCategory(JsonObject):
    name = StringProperty()
    product_tax_code = StringProperty()
    description = StringProperty()

class TaxJarCategories(TaxJarIterable):
    def handle_response(self, response):
        self.data = [TaxJarCategory(r) for r in response]
        return self
