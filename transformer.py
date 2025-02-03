class Transformer:
    def __init__(self, operation, factor=None):
        self.operation = operation
        self.factor = factor

    def apply(self, data):
        if self.operation == "multiply" and self.factor:
            return [str(int(line.strip()) * self.factor) + '\n' for line in data]
        return data
