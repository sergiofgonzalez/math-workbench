from abc import ABCMeta, abstractmethod

class Vector(metaclass=ABCMeta):

    @abstractmethod
    def scale(self, scalar):
        pass

    @abstractmethod
    def add(self, other):
        pass

    @classmethod
    @abstractmethod
    def zero(cls):
        pass

    def __neg__(self):
        return self.scale(-1)

    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise TypeError('scalar multiplication expects a numeric scalar')

        return self.scale(scalar)

    def __rmul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise TypeError('scalar multiplication expects a numeric scalar')

        return self.scale(scalar)

    def __add__(self, v2):
        if not self.__class__ in v2.__class__.mro():
            raise TypeError('__add__: given vector does not seem to be a compatible class')

        return self.add(v2)
    
    def subtract(self, other):
        if not self.__class__ in other.__class__.mro():
            raise TypeError('subtract: given vector does not seem to be a compatible class')

        return self.add(-1 * other)


    def __sub__(self, other):
        if not self.__class__ in other.__class__.mro():
            raise TypeError('__sub__: given vector does not seem to be a compatible class')

        return self.subtract(other)

    # added in Exercise 6.7
    def __truediv__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise TypeError('scalar division expects a numeric scalar')

        return self.scale(1.0 / scalar)