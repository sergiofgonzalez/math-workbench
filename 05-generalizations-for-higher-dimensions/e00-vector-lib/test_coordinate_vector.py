import unittest  # https://docs.python.org/3/library/unittest.html
from math import isclose
from random import uniform
from coordinate_vector import CoordinateVector
from test_vector import VectorTestCase

class CoordinateVectorTest(VectorTestCase):

    def random_coordinates(self, dimension):
        if not isinstance(dimension, int):
            raise TypeError('random_coordinates expects an int as dimension')
        
        coords = [self.random_scalar() for i in range(0, dimension)]
        return coords              

    def approx_equal(self, v, w):
        if (not CoordinateVector in v.__class__.mro()) or (not CoordinateVector in w.__class__.mro()):
            raise TypeError('approx_equal requires coordinate vectors')

        if not v.dimension() == w.dimension():
            raise TypeError('approx_equal requires coordinate vectors of the same dimension')
        
        return all(isclose(coord_v, coord_w) for coord_v, coord_w in zip(v.coordinates, w.coordinates))