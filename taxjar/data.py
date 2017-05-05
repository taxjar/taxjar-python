class TaxJarData(object):
    def __init__(self, values):
        self.handle_response(values)

    def handle_response(self, response_dict):
        for key in response_dict:
            setattr(self, key, response_dict[key])
        return self

    def __repr__(self):
        string = "<{} {}>".format(type(self).__name__, str(vars(self)))
        return string

class TaxJarIterable():
    def __init__(self, values):
        self.current = 0
        self.handle_response(values)

    def handle_response(self, response):
        self.data = response

    def __iter__(self):
        return self

    def next(self):
        return self.__next__()

    def __next__(self):
        try:
            result = self.data[self.current]
        except IndexError:
            raise StopIteration
        self.current += 1
        return result

    def __repr__(self):
        return str(self.data)

class TaxJarCategory(TaxJarData):
    pass

class TaxJarCategories(TaxJarIterable):
    def handle_response(self, response):
        self.data = [TaxJarCategory(r) for r in response]
        return self

class TaxJarRate(TaxJarData):
    pass

class TaxJarTax(TaxJarData):
    pass

class TaxJarOrders(TaxJarIterable):
    def handle_response(self, response):
        self.data = response
        return self

class TaxJarOrder(TaxJarData):
    pass

class TaxJarRegion(TaxJarData):
    pass

class TaxJarRegions(TaxJarIterable):
    def handle_response(self, response):
        self.data = [TaxJarRegion(r) for r in response]
        return self

class TaxJarValidation(TaxJarData):
    pass

class TaxJarSummaryRate(TaxJarData):
    pass

class TaxJarSummaryRates(TaxJarIterable):
    def handle_response(self, response):
        self.data = [TaxJarSummaryRate(r) for r in response]
        return self
