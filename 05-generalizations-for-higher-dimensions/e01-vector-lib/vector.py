from abc import ABCMeta, abstractmethod

class Vector(metaclass=ABCMeta):

    @abstractmethod
    def scale(self, scalar):
        pass

    @abstractmethod
    def add(self, other):
        pass

    def __mul__(self, scalar):
        return self.scale(scalar)

    def __rmul__(self, scalar):
        return self.scale(scalar)

    def __add__(self, v2):
        return self.add(v2)
    
    def subtract(self, other):
        return self.add(-1 * other)

    def __sub__(self, other):
        return self.subtract(other)