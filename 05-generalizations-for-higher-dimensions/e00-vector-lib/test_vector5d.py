import unittest  # https://docs.python.org/3/library/unittest.html
from math import isclose, pi
from vector5d import Vec5
from test_coordinate_vector import CoordinateVectorTest
from vector2d import Vec2
from coordinate_vector import CoordinateVector

class Vec5TestCase(CoordinateVectorTest):

    def test_scalar_rmult_args(self):
        with self.assertRaises(TypeError, msg='should raise TypeError when passing numeric scalar'):
            u = Vec5(*self.random_coordinates(5))
            s = 'a'
            s * u

    def test_scalar_mult_args(self):
        with self.assertRaises(TypeError, msg='should raise TypeError when passing numeric scalar'):
            u = Vec5(*self.random_coordinates(5))
            s = 'a'
            u * s

    def test_add_incompatible_types(self):
        with self.assertRaises(TypeError, msg='should raise TypeError when not compatible class'):        
            u = Vec5(*self.random_coordinates(5))
            v = 1
            u + v

    def test_add_incompatible_subclasses(self):
        def random_vec2():
            return Vec2(self.random_scalar(), self.random_scalar())

        with self.assertRaises(TypeError, msg='should raise TypeError when not compatible subclasses'):        
            u = Vec5(*self.random_coordinates(5))
            v = random_vec2()
            u + v

    def test_mult_incompatible_types(self):
        class A():
            def sayHello(self):
                return 'hello'

        with self.assertRaises(TypeError, msg='should raise TypeError when not compatible class'):        
            u = Vec5(*self.random_coordinates(5))
            v = A()
            u + v

    def test_sub_incompatible_types(self):
        with self.assertRaises(TypeError, msg='should raise TypeError when not compatible class'):        
            u = Vec5(*self.random_coordinates(5))
            v = 'v'
            u - v

    def test_vector6d_is_vector_space(self):
        for _ in range(0, 100):
            a, b = self.random_scalar(), self.random_scalar()
            u, v, w = Vec5(*self.random_coordinates(5)), Vec5(*self.random_coordinates(5)), Vec5(*self.random_coordinates(5))
            self.check_vector_space_rules(self.approx_equal, a, b, u, v, w)

    def test_zero_vector(self):
        self.assertEqual(Vec5.zero(), Vec5(0, 0, 0, 0, 0))

    def test_negate_vector(self):
        self.assertEqual(-Vec5(-1, 2, -3, 4, -5), Vec5(1, -2, 3, -4, 5))

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

        self.assertFalse(Vec5(1, 2, 3, 4, 5) == Vec7(1, 2, 3, 4, 5, 6, 7))
        self.assertFalse(Vec7(1, 2, 3, 4, 5, 6, 7) == Vec5(1, 2, 3, 4, 5))

    def test_add_between_classes(self):
        class Vec7(CoordinateVector):
            @classmethod
            def dimension(cls):
                return 7

            @classmethod
            def zero(cls):
                coords = tuple(0 for _ in range(0, cls.dimension()))
                return Vec7(*coords)

        with self.assertRaises(TypeError, msg='should raise TypeError when not compatible class'):        
            Vec5(1, 2, 3, 4, 5) + Vec7(1, 2, 3, 4, 5, 6, 7)

    def test_add_between_classes_2(self):
        class Vec7(CoordinateVector):
            @classmethod
            def dimension(cls):
                return 7

            @classmethod
            def zero(cls):
                coords = tuple(0 for _ in range(0, cls.dimension()))
                return Vec7(*coords)

        with self.assertRaises(TypeError, msg='should raise TypeError when not compatible class'):        
            Vec7(1, 2, 3, 4, 5, 6, 7) + Vec5(1, 2, 3, 4, 5)

    # added in exercise 6.7
    def test_scalar_division(self):
        self.approx_equal(Vec5(1, -2, 3, -4, pi) / 3.25, Vec5(1 / 3.25, -2 / 3.25, 3 / 3.25, -4 / 3.25, pi / 3.25))     

if __name__ == '__main__':
    unittest.main()
