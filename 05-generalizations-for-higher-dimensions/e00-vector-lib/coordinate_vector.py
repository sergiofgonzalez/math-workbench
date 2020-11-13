from vector import Vector
from my_vectors import add, scale
from abc import abstractmethod

class CoordinateVector(Vector):

    @classmethod
    @abstractmethod
    def zero(cls):
        pass

    @classmethod
    @abstractmethod
    def dimension(self):
        pass

    def __init__(self, *coordinates):
        if len(coordinates) != self.__class__.dimension():
            raise TypeError('CoordinateVector constructor was expecting a {} coordinate(s)'.format(self.__class__.dimension()))

        self.coordinates = tuple(x for x in coordinates)

    def add(self, other):
        # author used a one-liner, but these three lines make it easier to see what's going on
        coordinate_sum_as_tuple = add(self.coordinates, other.coordinates)
        sum_as_concrete_coordinate_vector = self.__class__(*coordinate_sum_as_tuple)        
        return sum_as_concrete_coordinate_vector

    def scale(self, scalar):
        # author used a one-liner, but these three lines make it easier to see what's going on        # return self.__class__(*scale(scalar, self.coordinates))
        coordinate_scalar_product_as_tuple = scale(scalar, self.coordinates)
        scalar_product_as_concrete_coordinate_vector = self.__class__(*coordinate_scalar_product_as_tuple)
        return scalar_product_as_concrete_coordinate_vector

    def __repr__(self):
        return '{}{}'.format(self.__class__.__qualname__, self.coordinates)

    def __eq__(self, other):
        if not self.__class__ in other.__class__.mro():
            return False
        else:        
            return self.coordinates == other.coordinates