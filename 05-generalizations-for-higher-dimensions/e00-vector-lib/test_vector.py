import unittest  # https://docs.python.org/3/library/unittest.html
from math import isclose
from random import uniform
from vector import Vector

class VectorTestCase(unittest.TestCase):

    def random_scalar(self):
        return uniform(-10, 10)

    def check_vector_space_rules(self, eqFn, a, b, u, v, w):
        self.assertTrue(eqFn(u + v, v + u))
        self.assertTrue(eqFn(u + (v + w), (u + v) + w))
        self.assertTrue(eqFn(a * (b * v), (a * b) * v))
        self.assertTrue(eqFn(1 * v, v))
        self.assertTrue(eqFn((a + b) * v, a * v + b * v))
        self.assertTrue(eqFn(a * v + a * w, a * (v + w)))
