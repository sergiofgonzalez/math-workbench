import unittest  # https://docs.python.org/3/library/unittest.html
from random import randint
from rational import Rational

class RationalTestCase(unittest.TestCase):

    def random_rational(self):

        random_numerator = randint(-15, 15)
        random_denominator = randint(1, 15)
        if (random_numerator == 0 or random_denominator == 0):
            return self.random_rational()
        return Rational(random_numerator, random_denominator)

    def test_create_valid_rational(self):
        r = Rational(3, 4)
        self.assertEqual(r.numerator, 3)
        self.assertEqual(r.denominator, 4)

    def test_create_valid_rational_from_int(self):
        r = Rational(5)
        self.assertEqual(r.numerator, 5)
        self.assertEqual(r.denominator, 1)

    def test_create_valid_rational_with_normalization(self):
        r = Rational(6, 3)
        self.assertEqual(r.numerator, 2)
        self.assertEqual(r.denominator, 1)

    def test_create_invalid_rational_from_float(self):
        with self.assertRaises(TypeError):
            Rational(1.5)

    # add tests
    def test_add(self):
        r = Rational(1, 2)
        q = Rational(2, 3)
        self.assertEqual(r + q, Rational(7, 6))

    def test_add_with_normalization(self):
        r = Rational(2, 3)
        q = Rational(1, 3)
        self.assertEqual(r + q, Rational(1))

    def test_add_with_int_on_right(self):
        r = Rational(2, 3)
        q = Rational(2)
        self.assertEqual(r + q, Rational(8, 3))

    def test_add_with_int_on_left(self):
        r = Rational(2)
        q = Rational(2, 3)
        self.assertEqual(r + q, Rational(8, 3))

    def test_add_random(self):
        r = self.random_rational()
        q = self.random_rational()
        self.assertEqual(r + q, Rational(r.numerator * q.denominator + q.numerator * r.denominator, r.denominator * q.denominator))

    def test_mult_random(self):
        r = self.random_rational()
        q = self.random_rational()
        self.assertEqual(r * q, Rational(r.numerator * q.numerator, r.denominator * q.denominator))

    def test_div(self):
        r = self.random_rational()
        q = self.random_rational()
        self.assertEqual(r / q, Rational(r.numerator * q.denominator, r.denominator * q.numerator))

    def test_subtract(self):
        r = self.random_rational()
        q = self.random_rational()
        self.assertEqual(r - q, Rational(r.numerator * q.denominator - q.numerator * r.denominator, r.denominator * q.denominator))

    def test_comparisons_1(self):
        r = Rational(1, 3)
        q = Rational(2, 3)
        self.assertTrue(r < q)
        self.assertTrue(r <= q)
        self.assertFalse(r == q)
        self.assertTrue(q > r)
        self.assertTrue(q >= r)

    def test_comparisons_2(self):
        r = Rational(1, 3)
        q = Rational(1, 3)
        self.assertFalse(r < q)
        self.assertTrue(r <= q)
        self.assertTrue(r == q)
        self.assertFalse(q > r)
        self.assertTrue(q >= r)

    def test_neg(self):
        r = self.random_rational()
        self.assertTrue(-r, Rational(-r.numerator, r.denominator))

    def test_exponent(self):
        r = self.random_rational()
        exponent = randint(1, 5)
        self.assertEqual(r ** exponent, Rational(r.numerator ** exponent, r.denominator ** exponent))

    def test_string_representation(self):
        r = self.random_rational()
        self.assertEqual(repr(r), '{}/{}'.format(r.numerator, r.denominator))

if __name__ == '__main__':
    unittest.main()