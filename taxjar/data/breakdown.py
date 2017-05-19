from jsonobject import JsonObject, ObjectProperty, ListProperty
from taxjar.data.float_property import TaxJarFloatProperty
from taxjar.data.breakdown_line_item import TaxJarBreakdownLineItem
from taxjar.data.shipping import TaxJarShipping

class TaxJarBreakdown(JsonObject):
    taxable_amount = TaxJarFloatProperty()
    tax_collectable = TaxJarFloatProperty()
    combined_tax_rate = TaxJarFloatProperty()
    state_taxable_amount = TaxJarFloatProperty()
    state_tax_rate = TaxJarFloatProperty()
    state_tax_collectable = TaxJarFloatProperty()
    county_taxable_amount = TaxJarFloatProperty()
    county_tax_rate = TaxJarFloatProperty()
    county_tax_collectable = TaxJarFloatProperty()
    city_taxable_amount = TaxJarFloatProperty()
    city_tax_rate = TaxJarFloatProperty()
    city_tax_collectable = TaxJarFloatProperty()
    special_district_taxable_amount = TaxJarFloatProperty()
    special_tax_rate = TaxJarFloatProperty()
    special_district_tax_collectable = TaxJarFloatProperty()
    country_taxable_amount = TaxJarFloatProperty()
    country_tax_rate = TaxJarFloatProperty()
    country_tax_collectable = TaxJarFloatProperty()
    gst_taxable_amount = TaxJarFloatProperty()
    gst_tax_rate = TaxJarFloatProperty()
    gst = TaxJarFloatProperty()
    pst_taxable_amount = TaxJarFloatProperty()
    pst_tax_rate = TaxJarFloatProperty()
    pst = TaxJarFloatProperty()
    qst_taxable_amount = TaxJarFloatProperty()
    qst_tax_rate = TaxJarFloatProperty()
    qst = TaxJarFloatProperty()

    shipping = ObjectProperty(TaxJarShipping)

    line_items = ListProperty(TaxJarBreakdownLineItem)
