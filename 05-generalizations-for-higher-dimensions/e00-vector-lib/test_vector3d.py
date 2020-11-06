import unittest  # https://docs.python.org/3/library/unittest.html
from math import isclose
from vector3d import Vec3
from vector2d import Vec2
from test_vector import VectorTestCase

class Vec3TestCase(VectorTestCase):

    def random_vec3(self):
        return Vec3(self.random_scalar(), self.random_scalar(), self.random_scalar())               

    def approx_equal_vec3(self, v, w):
        return isclose(v.x, w.x) and isclose(v.y, w.y) and isclose(v.z, w.z)

    def test_scalar_rmult_args(self):
        with self.assertRaises(TypeError, msg='shoud raise TypeError when passing numeric scalar'):
            u = self.random_vec3()
            s = 'a'
            s * u

    def test_scalar_mult_args(self):
        with self.assertRaises(TypeError, msg='shoud raise TypeError when passing numeric scalar'):
            u = self.random_vec3()
            s = 'a'
            u * s

    def test_add_incompatible_types(self):
        with self.assertRaises(TypeError, msg='shoud raise TypeError when not compatible class'):        
            u = self.random_vec3()
            v = 1
            u + v

    def test_add_incompatible_subclasses(self):
        def random_vec2():
            return Vec2(self.random_scalar(), self.random_scalar())

        with self.assertRaises(TypeError, msg='shoud raise TypeError when not compatible subclasses'):        
            u = self.random_vec3()
            v = random_vec2()
            u + v

    def test_mult_incompatible_types(self):
        class A():
            def sayHello(self):
                return 'hello'

        with self.assertRaises(TypeError, msg='shoud raise TypeError when not compatible class'):        
            u = self.random_vec3()
            v = A()
            u + v

    def test_sub_incompatible_types(self):
        with self.assertRaises(TypeError, msg='shoud raise TypeError when not compatible class'):        
            u = self.random_vec3()
            v = 'v'
            u + v

    def test_vector2d_is_vector_space(self):
        for _ in range(0, 100):
            a, b = self.random_scalar(), self.random_scalar()
            u, v, w = self.random_vec3(), self.random_vec3(), self.random_vec3()
            self.check_vector_space_rules(self.approx_equal_vec3, a, b, u, v, w)

    def test_zero_vector(self):
        self.assertEqual(Vec3.zero(), Vec3(0, 0, 0))

    def test_negate_vector(self):
        self.assertEqual(-Vec3(-1, 2, -3), Vec3(1, -2, 3))

    # added in exercise 6.6
    def test_eq_between_classes(self):
        self.assertFalse(Vec3(1, 2, 3) == Vec2(1, 2))

    def test_add_between_classes_1(self):
        with self.assertRaises(TypeError, msg='shoud raise TypeError when not compatible class'):        
            Vec2(1, 2) + Vec3(1, 2, 3)

    def test_add_between_classes_2(self):
        with self.assertRaises(TypeError, msg='shoud raise TypeError when not compatible class'):        
            Vec3(1, 2, 3) + Vec2(1, 2)

if __name__ == '__main__':
    unittest.main()
