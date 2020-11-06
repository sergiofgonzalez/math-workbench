import unittest  # https://docs.python.org/3/library/unittest.html
from math import isclose
from random import uniform
from vector2d import Vec2
from test_vector import VectorTestCase

class Vec2TestCase(VectorTestCase):

    def random_vec2(self):
        return Vec2(self.random_scalar(), self.random_scalar())               

    def approx_equal_vec2(self, v, w):
        return isclose(v.x, w.x) and isclose(v.y, w.y)

    def test_scalar_rmult_args(self):
        with self.assertRaises(TypeError, msg='shoud raise TypeError when passing numeric scalar'):
            u = self.random_vec2()
            s = 'a'
            s * u

    def test_scalar_mult_args2(self):
        with self.assertRaises(TypeError, msg='shoud raise TypeError when passing numeric scalar'):
            u = self.random_vec2()
            s = 'a'
            u * s

    def test_add_incompatible_types(self):
        with self.assertRaises(TypeError, msg='shoud raise TypeError when not compatible class'):        
            u = self.random_vec2()
            v = 1
            u + v

    def test_mult_incompatible_types(self):
        class A():
            def sayHello(self):
                return 'hello'

        with self.assertRaises(TypeError, msg='shoud raise TypeError when not compatible class'):        
            u = self.random_vec2()
            v = A()
            u + v

    def test_sub_incompatible_types(self):
        with self.assertRaises(TypeError, msg='shoud raise TypeError when not compatible class'):        
            u = self.random_vec2()
            v = 'v'
            u + v

    def test_vector2d_is_vector_space(self):
        for _ in range(0, 100):
            a, b = self.random_scalar(), self.random_scalar()
            u, v, w = self.random_vec2(), self.random_vec2(), self.random_vec2()
            self.check_vector_space_rules(self.approx_equal_vec2, a, b, u, v, w)



if __name__ == '__main__':
    unittest.main()
