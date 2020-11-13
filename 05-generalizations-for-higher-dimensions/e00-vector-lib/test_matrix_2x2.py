import unittest  # https://docs.python.org/3/library/unittest.html
from math import isclose, pi
from test_vector_matrix import MatrixTest
from vector_matrix_2x2 import Matrix_2x2
from vector2d import Vec2

class Matrix2x2TestCase(MatrixTest):

    def test_incorrect_matrix_cannot_be_built(self):
        with self.assertRaises(TypeError, msg='should raise TypeError when passing incorrect items'):
            Matrix_2x2(self.random_items(rows=1, columns=3))
        

    def test_add_happy_path(self):
        u = Matrix_2x2((
            (1, 2),
            (3, 4)
            ))
        
        v = Matrix_2x2(
            ((5, 6),
            (7, 8)))

        sum_matrix = u + v

        self.assertEqual(sum_matrix, Matrix_2x2(((6, 8), (10, 12))))

    def test_scalar_product_happy_path(self):
        u = Matrix_2x2(
            ((1, 2),
            (3, 4))
        )

        scalar = 2
        scalar_product_matrix = scalar * u

        self.assertTrue(scalar_product_matrix, Matrix_2x2(((2, 4), (6, 8))))

    def test_scalar_rmult_args(self):
        with self.assertRaises(TypeError, msg='should raise TypeError when passing numeric scalar'):
            u = Matrix_2x2(self.random_items(rows=2, columns=2))
            s = 'a'
            s * u

    def test_scalar_mult_args(self):
        with self.assertRaises(TypeError, msg='should raise TypeError when passing numeric scalar'):
            u = Matrix_2x2(self.random_items(rows=2, columns=2))
            s = 'a'
            u * s

    def test_add_incompatible_types(self):
        with self.assertRaises(TypeError, msg='should raise TypeError when not compatible class'):        
            u = Matrix_2x2(self.random_items(rows=2, columns=2))
            v = 1
            u + v

    def test_add_incompatible_subclasses(self):
        def random_vec2():
            return Vec2(self.random_scalar(), self.random_scalar())

        with self.assertRaises(TypeError, msg='should raise TypeError when not compatible subclasses'):        
            u = Matrix_2x2(self.random_items(rows=2, columns=2))
            v = random_vec2()
            u + v

    def test_mult_incompatible_types(self):
        class A():
            def sayHello(self):
                return 'hello'

        with self.assertRaises(TypeError, msg='should raise TypeError when not compatible class'):        
            u = Matrix_2x2(self.random_items(rows=2, columns=2))
            v = A()
            u + v

    def test_sub_incompatible_types(self):
        with self.assertRaises(TypeError, msg='should raise TypeError when not compatible class'):        
            u = Matrix_2x2(self.random_items(rows=2, columns=2))
            v = 'v'
            u - v

    def test_Matrix2x2_is_vector_space(self):
        for _ in range(0, 100):
            a, b = self.random_scalar(), self.random_scalar()
            u, v, w = Matrix_2x2(self.random_items(rows=2, columns=2)), Matrix_2x2(self.random_items(rows=2, columns=2)), Matrix_2x2(self.random_items(rows=2, columns=2))
            self.check_vector_space_rules(self.approx_equal, a, b, u, v, w)

    def test_zero_vector(self):
        self.assertEqual(Matrix_2x2.zero(), Matrix_2x2(((0, 0), (0, 0))))

    def test_negate_vector(self):
        self.assertEqual(-Matrix_2x2(((1, -2), (-3, 4))), Matrix_2x2(((-1, 2), (3, -4))))

    def test_scalar_division(self):
        self.approx_equal(Matrix_2x2(((1, -2), (pi, -4.56))) / 3.25, Matrix_2x2(((1 / 3.25, -2 / 3.25), (pi / 3.25, -4.56 / 3.25))))     

if __name__ == '__main__':
    unittest.main()
