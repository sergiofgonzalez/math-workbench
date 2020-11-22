import unittest  # https://docs.python.org/3/library/unittest.html
from math import isclose
from vector_linear_function import LinearFunction
from vector2d import Vec2
from test_vector import VectorTestCase

class LinearFunctionTestCase(VectorTestCase):

    def random_linear_function(self):
        return LinearFunction(self.random_scalar(), self.random_scalar())               

    def approx_equal_linear_function(self, f, g):
        if (not LinearFunction in f.__class__.mro()) or (not LinearFunction in f.__class__.mro()):
            raise TypeError('approx_equal requires coordinate vectors')
       
        return all([isclose(f.a, g.a), isclose(f.b, g.b)])

    def test_scalar_rmult_args(self):
        with self.assertRaises(TypeError, msg='should raise TypeError when passing numeric scalar'):
            u = self.random_linear_function()
            s = 'a'
            s * u

    def test_scalar_mult_args(self):
        with self.assertRaises(TypeError, msg='should raise TypeError when passing numeric scalar'):
            u = self.random_linear_function()
            s = 'a'
            u * s

    def test_add_incompatible_types(self):
        with self.assertRaises(TypeError, msg='should raise TypeError when not compatible class'):        
            u = self.random_linear_function()
            v = 1
            u + v

    def test_add_incompatible_subclasses(self):
        def random_vec2():
            return Vec2(self.random_scalar(), self.random_scalar())

        with self.assertRaises(TypeError, msg='should raise TypeError when not compatible subclasses'):        
            u = self.random_linear_function()
            v = random_vec2()
            u + v

    def test_mult_incompatible_types(self):
        class A():
            def sayHello(self):
                return 'hello'

        with self.assertRaises(TypeError, msg='should raise TypeError when not compatible class'):        
            u = self.random_linear_function()
            v = A()
            u + v

    def test_sub_incompatible_types(self):
        with self.assertRaises(TypeError, msg='should raise TypeError when not compatible class'):        
            u = self.random_linear_function()
            v = 'v'
            u + v

    def test_LinearFunction_is_vector_space(self):
        for _ in range(0, 100):
            a, b = self.random_scalar(), self.random_scalar()
            u, v, w = self.random_linear_function(), self.random_linear_function(), self.random_linear_function()
            self.check_vector_space_rules(self.approx_equal_linear_function, a, b, u, v, w)

    def test_zero_vector(self):
        self.assertEqual(LinearFunction.zero(), LinearFunction(0, 0))

    def test_negate_vector(self):
        f = LinearFunction(-1, 2)
        neg_f = LinearFunction(1, -2)
        self.assertEqual(-f, neg_f)

    def test_scalar_division(self):
        self.approx_equal_linear_function(LinearFunction(10, -4.4) / 2, LinearFunction(5, -2.2))

if __name__ == '__main__':
    unittest.main()
