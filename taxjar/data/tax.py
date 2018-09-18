from jsonobject import JsonObject, BooleanProperty, ObjectProperty, StringProperty
from taxjar.data.float_property import TaxJarFloatProperty
from taxjar.data.jurisdictions import TaxJarJurisdictions
from taxjar.data.breakdown import TaxJarBreakdown

class TaxJarTax(JsonObject):
    order_total_amount = TaxJarFloatProperty()
    shipping = TaxJarFloatProperty()
    taxable_amount = TaxJarFloatProperty()
    amount_to_collect = TaxJarFloatProperty()
    rate = TaxJarFloatProperty()

    has_nexus = BooleanProperty()
    freight_taxable = BooleanProperty()

    tax_source = StringProperty()

    jurisdictions = ObjectProperty(TaxJarJurisdictions)

    breakdown = ObjectProperty(TaxJarBreakdown)
