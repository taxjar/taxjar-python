from jsonobject import JsonObject, StringProperty, ListProperty, IntegerProperty
from taxjar.data.float_property import TaxJarFloatProperty

class TaxJarLineItem(JsonObject):
    # NB: SmartCalcs can return either string or integer
    # `id` is a valid property, but isn't enforced here
    # id = StringProperty()

    product_identifier = StringProperty()
    description = StringProperty()

    quantity = IntegerProperty()

    unit_price = TaxJarFloatProperty()
    discount = TaxJarFloatProperty()
    sales_tax = TaxJarFloatProperty()
