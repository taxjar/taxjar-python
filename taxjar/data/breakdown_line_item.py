from jsonobject import JsonObject
from taxjar.data.float_property import TaxJarFloatProperty

class TaxJarBreakdownLineItem(JsonObject):
    # NB: can return either string or integer
    # `id` is a valid property, but isn't enforced here
    # id = StringProperty()

    taxable_amount = TaxJarFloatProperty()
    tax_collectable = TaxJarFloatProperty()
    combined_tax_rate = TaxJarFloatProperty()
    state_taxable_amount = TaxJarFloatProperty()
    state_sales_tax_rate = TaxJarFloatProperty()
    state_amount = TaxJarFloatProperty()
    county_taxable_amount = TaxJarFloatProperty()
    county_tax_rate = TaxJarFloatProperty()
    county_amount = TaxJarFloatProperty()
    city_taxable_amount = TaxJarFloatProperty()
    city_tax_rate = TaxJarFloatProperty()
    city_amount = TaxJarFloatProperty()
    special_district_taxable_amount = TaxJarFloatProperty()
    special_tax_rate = TaxJarFloatProperty()
    special_district_amount = TaxJarFloatProperty()
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
