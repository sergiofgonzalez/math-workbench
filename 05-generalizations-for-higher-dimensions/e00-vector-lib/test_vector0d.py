import unittest  # https://docs.python.org/3/library/unittest.html
from math import isclose
from random import uniform
from vector0d import Vec0
from vector2d import Vec2
from vector3d import Vec3
from test_vector import VectorTestCase

class Vec0TestCase(VectorTestCase):

    def random_vec0(self):
        return Vec0()               

    def approx_equal_vec0(self, v, w):
        return v == w

    def test_scalar_rmult_args(self):
        with self.assertRaises(TypeError, msg='should raise TypeError when passing numeric scalar'):
            u = self.random_vec0()
            s = 'a'
            s * u

    def test_scalar_mult_args2(self):
        with self.assertRaises(TypeError, msg='should raise TypeError when passing numeric scalar'):
            u = self.random_vec0()
            s = 'a'
            u * s

    def test_add_incompatible_types(self):
        with self.assertRaises(TypeError, msg='should raise TypeError when not compatible class'):        
            u = self.random_vec0()
            v = 1
            u + v

    def test_mult_incompatible_types(self):
        class A():
            def sayHello(self):
                return 'hello'

        with self.assertRaises(TypeError, msg='should raise TypeError when not compatible class'):        
            u = self.random_vec0()
            v = A()
            u + v

    def test_sub_incompatible_types(self):
        with self.assertRaises(TypeError, msg='should raise TypeError when not compatible class'):        
            u = self.random_vec0()
            v = 'v'
            u + v

    def test_vector0d_is_vector_space(self):
        for _ in range(0, 100):
            a, b = self.random_scalar(), self.random_scalar()
            u, v, w = self.random_vec0(), self.random_vec0(), self.random_vec0()
            self.check_vector_space_rules(self.approx_equal_vec0, a, b, u, v, w)

    def test_zero_vector(self):
        self.assertEqual(Vec0.zero(), Vec0())

    def test_negate_vector(self):
        self.assertEqual(-Vec0(), Vec0())

   # added in exercise 6.6
    def test_eq_between_classes(self):
        self.assertFalse(Vec0() == Vec3(1, 2, 3))
        self.assertFalse(Vec3(1, 2, 3) == Vec0())        

    def test_add_between_classes_1(self):
        with self.assertRaises(TypeError, msg='should raise TypeError when not compatible class'):        
            Vec0() + Vec3(1, 2, 3)

    def test_add_between_classes_2(self):
        with self.assertRaises(TypeError, msg='should raise TypeError when not compatible class'):        
            Vec3(1, 2, 3) + Vec0()

    # added in exercise 6.7
    def test_scalar_division(self):
        self.approx_equal_vec0(Vec0() / 2, Vec0())        

if __name__ == '__main__':
    unittest.main()
