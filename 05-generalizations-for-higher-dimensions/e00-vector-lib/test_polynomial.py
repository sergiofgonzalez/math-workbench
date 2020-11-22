import unittest  # https://docs.python.org/3/library/unittest.html
from vector_polynomial import Polynomial
from test_vector import VectorTestCase

class PolynomialTestCase(VectorTestCase):

    def test_build_polynomial_3(self):
        poly = Polynomial(1, 2, 3)
        self.assertEqual(poly.__repr__(), '1 + 2x + 3x^2')

    def test_add_polys(self):
        p1 = Polynomial(1, 2, 3)
        p2 = Polynomial(4, 5)
        self.assertEqual(p1 + p2, Polynomial(5, 7, 3))

if __name__ == '__main__':
    unittest.main()
