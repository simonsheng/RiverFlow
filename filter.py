class Filter:
    def __init__(self, criteria):
        self.criteria = criteria

    def apply(self, data):
        return [line for line in data if eval(self.criteria)]
