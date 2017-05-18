class TaxJarIterable(object):
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
