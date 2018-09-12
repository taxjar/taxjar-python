from jsonobject import JsonObject, StringProperty

class TaxJarJurisdictions(JsonObject):
    country = StringProperty()
    state = StringProperty()
    county = StringProperty()
    city = StringProperty()
