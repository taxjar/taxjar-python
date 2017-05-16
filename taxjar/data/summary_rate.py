from jsonobject import JsonObject, StringProperty, ObjectProperty
from taxjar.data.iterable import TaxJarIterable
from taxjar.data.float_property import TaxJarFloatProperty

class TaxJarSummaryRateParent(JsonObject):
    country_code = StringProperty()
    country = StringProperty()
    region_code = StringProperty()
    region = StringProperty()

class TaxJarMinimumRate(TaxJarSummaryRateParent):
    label = StringProperty()
    rate = TaxJarFloatProperty()

class TaxJarAverageRate(TaxJarSummaryRateParent):
    label = StringProperty()
    rate = TaxJarFloatProperty()

class TaxJarSummaryRate(JsonObject):
    minimum_rate = ObjectProperty(TaxJarMinimumRate)
    average_rate = ObjectProperty(TaxJarAverageRate)

class TaxJarSummaryRates(TaxJarIterable):
    def handle_response(self, response):
        self.data = [TaxJarSummaryRate(r) for r in response]
        return self
