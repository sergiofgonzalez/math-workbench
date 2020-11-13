import unittest  # https://docs.python.org/3/library/unittest.html
from math import isclose
from vector_function2 import Function2
from test_vector import VectorTestCase
from math import sin
from my_plot import plot

class VectorFunction2TestCase(VectorTestCase):
    def approx_equal(self, v, w):
        
        if (not Function2 in v.__class__.mro()) or (not Function2 in w.__class__.mro()):
            raise TypeError('approx_equal requires compatible Function vectors')        
        
        num_samples = 10000
        samples = [(self.random_scalar(), self.random_scalar()) for _ in range(0, num_samples)]
        results = [isclose(v(x, y), w(x, y)) for x, y in samples]
        return all(results)

    def test_vector_function_creation_with_char(self):
        with self.assertRaises(TypeError, msg='should raise TypeError when passing non-function arg'):
            Function2('a')

    def test_vector_function_creation_with_num(self):
        with self.assertRaises(TypeError, msg='should raise TypeError when passing non-function arg'):
            Function2(2)

    def test_vector_function_creation_happy_path(self):
        def f(x, y):
            return x + y

        vector_f = Function2(f)
        self.assertEqual(vector_f(5, 7), 12)

    def test_vector_function_add_happy_path(self):
        def f(x, y):
            return x + y

        def g(x, y):
            return x + y + 1

        vector_f = Function2(f)
        vector_g = Function2(g)

        self.assertEqual((vector_f + vector_g)(5, 6), 23)

    def test_vector_function_mult_happy_path(self):
        def f(x, y):
            return x + y

        vector_f = Function2(f)

        self.assertEqual(5 * vector_f(5, 6), 55)

    def test_vector_negate_happy_path(self):
        def f(x, y):
            return x + y
        
        vector_f = Function2(f)

        self.assertEqual(-vector_f(5, 6), -11)

    def test_zero_function_happy_path(self):
        vector_f0 = Function2.zero()
        for _ in range(0, 1000):
            self.assertEqual(vector_f0(self.random_scalar(), self.random_scalar()), 0)

    def test_approx_equal_function_happy_path(self):
        f1 = Function2(lambda x, y: x + y + 1)
        f2 = Function2(lambda x, y: x + y + 0.5 * 2)
        self.assertTrue(self.approx_equal(f1, f2))

    def test_approx_equal_function_happy_path_2(self):
        f1 = Function2(lambda x, y: x + y + 1)
        f2 = Function2(lambda x, y: sin(x) + sin(y))
        self.assertFalse(self.approx_equal(f1, f2))

    def test_approx_equal_function_happy_path_3(self):
        f = Function2(lambda x, y: x + y)
        g = Function2(lambda x, y: x - y + 1)
        h = Function2(lambda x, y: 2 * x + 1)
        self.assertTrue(self.approx_equal(f + g, h))


if __name__ == '__main__':
    unittest.main()    