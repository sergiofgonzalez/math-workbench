import unittest  # https://docs.python.org/3/library/unittest.html
from math import isclose
from vector6d import Vec6
from test_coordinate_vector import CoordinateVectorTest
from vector2d import Vec2
from coordinate_vector import CoordinateVector

class Vec6TestCase(CoordinateVectorTest):

    def test_scalar_rmult_args(self):
        with self.assertRaises(TypeError, msg='shoud raise TypeError when passing numeric scalar'):
            u = Vec6(*self.random_coordinates(6))
            s = 'a'
            s * u

    def test_scalar_mult_args(self):
        with self.assertRaises(TypeError, msg='shoud raise TypeError when passing numeric scalar'):
            u = Vec6(*self.random_coordinates(6))
            s = 'a'
            u * s

    def test_add_incompatible_types(self):
        with self.assertRaises(TypeError, msg='shoud raise TypeError when not compatible class'):        
            u = Vec6(*self.random_coordinates(6))
            v = 1
            u + v

    def test_add_incompatible_subclasses(self):
        def random_vec2():
            return Vec2(self.random_scalar(), self.random_scalar())

        with self.assertRaises(TypeError, msg='shoud raise TypeError when not compatible subclasses'):        
            u = Vec6(*self.random_coordinates(6))
            v = random_vec2()
            u + v

    def test_mult_incompatible_types(self):
        class A():
            def sayHello(self):
                return 'hello'

        with self.assertRaises(TypeError, msg='shoud raise TypeError when not compatible class'):        
            u = Vec6(*self.random_coordinates(6))
            v = A()
            u + v

    def test_sub_incompatible_types(self):
        with self.assertRaises(TypeError, msg='shoud raise TypeError when not compatible class'):        
            u = Vec6(*self.random_coordinates(6))
            v = 'v'
            u + v

    def test_vector6d_is_vector_space(self):
        for _ in range(0, 100):
            a, b = self.random_scalar(), self.random_scalar()
            u, v, w = Vec6(*self.random_coordinates(6)), Vec6(*self.random_coordinates(6)), Vec6(*self.random_coordinates(6))
            self.check_vector_space_rules(self.approx_equal, a, b, u, v, w)

    def test_zero_vector(self):
        self.assertEqual(Vec6.zero(), Vec6(0, 0, 0, 0, 0, 0))

    def test_negate_vector(self):
        self.assertEqual(-Vec6(-1, 2, -3, 4, -5, 6), Vec6(1, -2, 3, -4, 5, -6))

    # added in exercise 6.6
    def test_eq_between_classes(self):
        class Vec7(CoordinateVector):
            @classmethod
            def dimension(cls):
                return 7

            @classmethod
            def zero(cls):
                coords = tuple(0 for _ in range(0, cls.dimension()))
                return Vec7(*coords)

        self.assertFalse(Vec6(1, 2, 3, 4, 5, 6) == Vec7(1, 2, 3, 4, 5, 6, 7))
        self.assertFalse(Vec7(1, 2, 3, 4, 5, 6, 7) == Vec7(1, 2, 3, 4, 5, 6))

    def test_add_between_classes(self):
        class Vec7(CoordinateVector):
            @classmethod
            def dimension(cls):
                return 7

            @classmethod
            def zero(cls):
                coords = tuple(0 for _ in range(0, cls.dimension()))
                return Vec7(*coords)

        with self.assertRaises(TypeError, msg='shoud raise TypeError when not compatible class'):        
            Vec6(1, 2, 3, 4, 5, 6) + Vec7(1, 2, 3, 4, 5, 6, 7)

    def test_add_between_classes_2(self):
        class Vec7(CoordinateVector):
            @classmethod
            def dimension(cls):
                return 7

            @classmethod
            def zero(cls):
                coords = tuple(0 for _ in range(0, cls.dimension()))
                return Vec7(*coords)

        with self.assertRaises(TypeError, msg='shoud raise TypeError when not compatible class'):        
            Vec7(1, 2, 3, 4, 5, 6, 7) + Vec6(1, 2, 3, 4, 5, 6)

if __name__ == '__main__':
    unittest.main()
