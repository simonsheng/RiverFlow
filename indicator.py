from abc import ABC, abstractmethod

# Define the base Filter interface
class Filter(ABC):
    @abstractmethod
    def apply(self, item):
        pass

# Implement the StringMatcher indicator
class StringMatcher(Filter):
    def __init__(self, pattern):
        self.pattern = pattern

    def apply(self, item):
        return self.pattern in item

# Implement the Persister indicator
class Persister(Filter):
    def __init__(self, should_persist):
        self.should_persist = should_persist

    def apply(self, item):
        return self.should_persist

# Implement the CompositeFilter to combine multiple indicators
class CompositeFilter(Filter):
    def __init__(self):
        self.filters = []

    def add_filter(self, filter):
        self.filters.append(filter)

    def apply(self, item):
        return all(filter.apply(item) for filter in self.filters)