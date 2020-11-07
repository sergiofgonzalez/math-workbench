import unittest  # https://docs.python.org/3/library/unittest.html
from math import isclose
from random import uniform
from vector1d import Vec1
from vector3d import Vec3
from test_vector import VectorTestCase

class Vec1TestCase(VectorTestCase):

    def random_vec1(self):
        return Vec1(self.random_scalar())               

    def approx_equal_vec1(self, v, w):
        return isclose(v.x, w.x)

    def test_scalar_rmult_args(self):
        with self.assertRaises(TypeError, msg='should raise TypeError when passing numeric scalar'):
            u = self.random_vec1()
            s = 'a'
            s * u

    def test_scalar_mult_args2(self):
        with self.assertRaises(TypeError, msg='should raise TypeError when passing numeric scalar'):
            u = self.random_vec1()
            s = 'a'
            u * s

    def test_add_incompatible_types(self):
        with self.assertRaises(TypeError, msg='should raise TypeError when not compatible class'):        
            u = self.random_vec1()
            v = 1
            u + v

    def test_mult_incompatible_types(self):
        class A():
            def sayHello(self):
                return 'hello'

        with self.assertRaises(TypeError, msg='should raise TypeError when not compatible class'):        
            u = self.random_vec1()
            v = A()
            u + v

    def test_sub_incompatible_types(self):
        with self.assertRaises(TypeError, msg='should raise TypeError when not compatible class'):        
            u = self.random_vec1()
            v = 'v'
            u + v

    def test_vector2d_is_vector_space(self):
        for _ in range(0, 100):
            a, b = self.random_scalar(), self.random_scalar()
            u, v, w = self.random_vec1(), self.random_vec1(), self.random_vec1()
            self.check_vector_space_rules(self.approx_equal_vec1, a, b, u, v, w)

    def test_zero_vector(self):
        self.assertEqual(Vec1.zero(), Vec1(0))

    def test_negate_vector(self):
        self.assertEqual(-Vec1(-1), Vec1(1))

   # added in exercise 6.6
    def test_eq_between_classes(self):
        self.assertFalse(Vec1(1) == Vec3(1, 2, 3))
        self.assertFalse(Vec3(1, 2, 3) == Vec1(1))        

    def test_add_between_classes_1(self):
        with self.assertRaises(TypeError, msg='should raise TypeError when not compatible class'):        
            Vec1(1) + Vec3(1, 2, 3)

    def test_add_between_classes_2(self):
        with self.assertRaises(TypeError, msg='should raise TypeError when not compatible class'):        
            Vec3(1, 2, 3) + Vec1(1)

    # added in exercise 6.7
    def test_scalar_division(self):
        self.approx_equal_vec1(Vec1(-4.4) / 2, Vec1(-2.2))        

if __name__ == '__main__':
    unittest.main()
