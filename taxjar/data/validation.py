from jsonobject import JsonObject, StringProperty, ObjectProperty, BooleanProperty

class TaxJarValidationParent(JsonObject):
    valid = BooleanProperty()
    exists = BooleanProperty()
    vies_available = BooleanProperty()

class TaxJarViesResponse(TaxJarValidationParent):
    vat_number = StringProperty()
    request_date = StringProperty()
    valid = BooleanProperty()
    name = StringProperty()
    address = StringProperty()

class TaxJarValidation(TaxJarValidationParent):
    vies_response = ObjectProperty(TaxJarViesResponse)
