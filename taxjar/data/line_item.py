from jsonobject import JsonObject, StringProperty, ListProperty, IntegerProperty
from taxjar.data.float_property import TaxJarFloatProperty

class TaxJarLineItem(JsonObject):
    id = StringProperty()
    product_identifier = StringProperty()
    description = StringProperty()

    quantity = IntegerProperty()

    unit_price = TaxJarFloatProperty()
    discount = TaxJarFloatProperty()
    sales_tax = TaxJarFloatProperty()
