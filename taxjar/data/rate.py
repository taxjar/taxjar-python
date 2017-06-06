from jsonobject import JsonObject, StringProperty, BooleanProperty
from taxjar.data.float_property import TaxJarFloatProperty

class TaxJarRate(JsonObject):
    zip = StringProperty()
    state = StringProperty()
    county = StringProperty()
    city = StringProperty()
    country = StringProperty()
    name = StringProperty()

    country_rate = TaxJarFloatProperty()
    state_rate = TaxJarFloatProperty()
    county_rate = TaxJarFloatProperty()
    city_rate = TaxJarFloatProperty()
    combined_district_rate = TaxJarFloatProperty()
    combined_rate = TaxJarFloatProperty()

    standard_rate = TaxJarFloatProperty()
    reduced_rate = TaxJarFloatProperty()
    super_reduced_rate = TaxJarFloatProperty()
    parking_rate = TaxJarFloatProperty()
    distance_sale_threshold = TaxJarFloatProperty()

    freight_taxable = BooleanProperty()
