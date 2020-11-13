import unittest  # https://docs.python.org/3/library/unittest.html
from math import isclose
from vector_function import Function
from test_vector import VectorTestCase
from math import sin
from my_plot import plot

class VectorFunctionTestCase(VectorTestCase):

    def approx_equal(self, v, w):
        if (not Function in v.__class__.mro()) or (not Function in w.__class__.mro()):
            raise TypeError('approx_equal requires compatible Function vectors')        
        
        num_samples = 10000
        samples = [self.random_scalar() for _ in range(0, num_samples)]
        results = [isclose(v(x), w(x)) for x in samples]
        return all(results)

    def test_vector_function_creation_with_char(self):
        with self.assertRaises(TypeError, msg='should raise TypeError when passing non-function arg'):
            Function('a')

    def test_vector_function_creation_with_num(self):
        with self.assertRaises(TypeError, msg='should raise TypeError when passing non-function arg'):
            Function(2)

    def test_vector_function_creation_happy_path(self):
        def f(x):
            return x

        vector_f = Function(f)
        self.assertEqual(vector_f(5), 5)

    def test_vector_function_add_happy_path(self):
        def f(x):
            return x

        def g(x):
            return x + 1

        vector_f = Function(f)
        vector_g = Function(g)

        self.assertEqual((vector_f + vector_g)(5), 11)

    def test_vector_function_mult_happy_path(self):
        def f(x):
            return x

        vector_f = Function(f)

        self.assertEqual(5 * vector_f(5), 25)

    def test_vector_negate_happy_path(self):
        def f(x):
            return x
        
        vector_f = Function(f)

        self.assertEqual(-vector_f(5), -5)

    def test_zero_function_happy_path(self):
        vector_f0 = Function.zero()
        for _ in range(0, 1000):
            self.assertEqual(vector_f0(self.random_scalar()), 0)

    def test_plot_happy_path(self):
        f = Function(lambda x: 0.5 * x + 3)
        g = Function(sin)

        plot([f, g, f + g, 3 * g], -10, 10, 'Visualizing several `Function(Vector)`')

    def test_approx_equal_function_happy_path(self):
        f1 = Function(lambda x: x + 1)
        f2 = Function(lambda x: x + 0.5 * 2)
        self.assertTrue(self.approx_equal(f1, f2))

    def test_approx_equal_function_happy_path_2(self):
        f1 = Function(lambda x: x + 1)
        f2 = Function(sin)
        self.assertFalse(self.approx_equal(f1, f2))

    def test_approx_equal_is_faulty(self):
        f1 = Function(lambda x: (x * x) / x)
        f2 = Function(lambda x: x)

        # this should be False, as the functions are clearly different and yet
        # our function returns true
        self.assertFalse(self.approx_equal(f1, f2), 'This is expected as function equality is undecidable')

if __name__ == '__main__':
    unittest.main()    