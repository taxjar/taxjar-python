from jsonobject import JsonObject, StringProperty

class TaxJarExemptRegion(JsonObject):
    country = StringProperty()
    state = StringProperty()
