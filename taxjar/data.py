class TaxJarData:
    def __init__(self, values):
        self.handle_response(values)

    def handle_response(self, response_dict):
        for key in response_dict:
            setattr(self, key, response_dict[key])
        return self

    def __repr__(self):
        string = "<{} {}>".format(type(self).__name__, str(vars(self)))
        return string


class TaxJarCategory(TaxJarData):
    pass

class TaxJarCategories(TaxJarData):
    def handle_response(self, response):
        self.data = [TaxJarCategory(r) for r in response]
        return self

class TaxJarRate(TaxJarData):
    pass

class TaxJarTax(TaxJarData):
    pass

class TaxJarOrders(TaxJarData):
    def handle_response(self, response):
        self.data = response
        return self

class TaxJarOrder(TaxJarData):
    pass

class TaxJarRegion(TaxJarData):
    pass

class TaxJarRegions(TaxJarData):
    def handle_response(self, response):
        self.data = [TaxJarRegion(r) for r in response]
        return self

class TaxJarValidation(TaxJarData):
    pass

class TaxJarSummaryRate(TaxJarData):
    pass

class TaxJarSummaryRates(TaxJarData):
    def handle_response(self, response):
        self.data = [TaxJarSummaryRate(r) for r in response]
        return self
