from jsonobject import JsonObject, IntegerProperty, StringProperty, ListProperty
from taxjar.data.line_item import TaxJarLineItem
from taxjar.data.iterable import TaxJarIterable
from taxjar.data.float_property import TaxJarFloatProperty

class TaxJarOrder(JsonObject):
    user_id = IntegerProperty()

    transaction_id = StringProperty()
    transaction_date = StringProperty()
    from_country = StringProperty()
    from_zip = StringProperty()
    from_state = StringProperty()
    from_city = StringProperty()
    from_street = StringProperty()
    to_country = StringProperty()
    to_zip = StringProperty()
    to_state = StringProperty()
    to_city = StringProperty()
    to_street = StringProperty()

    amount = TaxJarFloatProperty()
    shipping = TaxJarFloatProperty()
    sales_tax = TaxJarFloatProperty()

    line_items = ListProperty(TaxJarLineItem)

class TaxJarOrders(TaxJarIterable):
    def handle_response(self, response):
        self.data = response
        return self
