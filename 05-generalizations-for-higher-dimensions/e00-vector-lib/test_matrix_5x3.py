import unittest  # https://docs.python.org/3/library/unittest.html
from math import isclose, pi
from test_vector_matrix import MatrixTest
from vector_matrix_5x3 import Matrix_5x3
from vector_matrix_2x2 import Matrix_2x2
from vector3d import Vec3
from vector5d import Vec5

class Matrix5x3TestCase(MatrixTest):

    # added in Exercise 6.20
    def test_multiply_matrix_by_vector(self):
        m = Matrix_5x3((
            (1, 2, 3),
            (4, 5, 6),
            (7, 8, 9),
            (10, 11, 12),
            (13, 14, 15)
            ))

        v = Vec3(1, 1, 1)

        result = m * v
        self.assertEqual(result, Vec5(6, 15, 24, 33, 42))

    def test_multiply_matrix_by_scalar_happy_path(self):
        m = Matrix_5x3((
            (1, 2, 3),
            (4, 5, 6),
            (7, 8, 9),
            (10, 11, 12),
            (13, 14, 15)
            ))    

        result = 2 * m
        expected_result = Matrix_5x3((
            (2, 4, 6),
            (8, 10, 12),
            (14, 16, 18),
            (20, 22, 24),
            (26, 28, 30)
        ))
        self.assertEqual(result, expected_result)

    def test_multiply_matrix_by_scalar_on_right(self):
        m = Matrix_5x3((
            (1, 2, 3),
            (4, 5, 6),
            (7, 8, 9),
            (10, 11, 12),
            (13, 14, 15)
            ))    

        result = m * 2
        expected_result = Matrix_5x3((
            (2, 4, 6),
            (8, 10, 12),
            (14, 16, 18),
            (20, 22, 24),
            (26, 28, 30)
        ))
        self.assertEqual(result, expected_result)

    def test_incorrect_matrix_cannot_be_built(self):
        with self.assertRaises(TypeError, msg='should raise TypeError when passing incorrect items'):
            Matrix_5x3(self.random_items(rows=5, columns=5))

    def test_add_happy_path(self):
        u = Matrix_5x3((
            (1, 2, 3),
            (4, 5, 6),
            (7, 8, 9),
            (10, 11, 12),
            (13, 14, 15)
            ))
        
        v = Matrix_5x3((
            (16, 17, 18),
            (19, 20, 21),
            (22, 23, 24),
            (25, 26, 27),
            (28, 29, 30)
            ))

        sum_matrix = u + v

        self.assertEqual(sum_matrix, Matrix_5x3((
            (17, 19, 21), 
            (23, 25, 27),
            (29, 31, 33),
            (35, 37, 39),
            (41, 43, 45)
            ))
        )

    def test_scalar_product_happy_path(self):
        u = Matrix_5x3((
            (1, 2, 3),
            (4, 5, 6),
            (7, 8, 9),
            (10, 11, 12),
            (13, 14, 15)
            ))

        scalar = 2
        scalar_product_matrix = scalar * u

        self.assertTrue(scalar_product_matrix, Matrix_5x3((
            (2, 4, 6),
            (8, 10, 12),
            (14, 16, 18),
            (20, 22, 24),
            (26, 28, 30)
            )
        ))

    def test_scalar_rmult_args(self):
        with self.assertRaises(TypeError, msg='should raise TypeError when passing numeric scalar'):
            u = Matrix_5x3(self.random_items(rows=5, columns=3))
            s = 'a'
            s * u

    def test_scalar_mult_args(self):
        with self.assertRaises(TypeError, msg='should raise TypeError when passing numeric scalar'):
            u = Matrix_5x3(self.random_items(rows=5, columns=3))
            s = 'a'
            u * s

    def test_add_incompatible_types(self):
        with self.assertRaises(TypeError, msg='should raise TypeError when not compatible class'):        
            u = Matrix_5x3(self.random_items(rows=5, columns=3))
            v = 1
            u + v

    def test_add_incompatible_subclasses(self):
        with self.assertRaises(TypeError, msg='should raise TypeError when not compatible subclasses'):        
            u = Matrix_5x3(self.random_items(rows=5, columns=3))
            v = Matrix_2x2(self.random_items(rows=2, columns=2))
            u + v

    def test_mult_incompatible_types(self):
        class A():
            def sayHello(self):
                return 'hello'

        with self.assertRaises(TypeError, msg='should raise TypeError when not compatible class'):        
            u = Matrix_5x3(self.random_items(rows=5, columns=3))
            v = A()
            u + v

    def test_sub_incompatible_types(self):
        with self.assertRaises(TypeError, msg='should raise TypeError when not compatible class'):        
            u = Matrix_5x3(self.random_items(rows=5, columns=3))
            v = 'v'
            u - v

    def test_Matrix5x3_is_vector_space(self):
        for _ in range(0, 100):
            a, b = self.random_scalar(), self.random_scalar()
            u, v, w = Matrix_5x3(self.random_items(rows=5, columns=3)), Matrix_5x3(self.random_items(rows=5, columns=3)), Matrix_5x3(self.random_items(rows=5, columns=3))
            self.check_vector_space_rules(self.approx_equal, a, b, u, v, w)

    def test_zero_vector(self):
        self.assertEqual(Matrix_5x3.zero(), Matrix_5x3(((0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0))))

    def test_negate_vector(self):
        m = (
            (1, -2, 3),
            (-4, 5, -6),
            (7, -8, 9),
            (-10, 11, -12),
            (13, -14, 15)
        )

        m_negated = (
            (-1, 2, -3),
            (4, -5, 6),
            (-7, 8, -9),
            (10, -11, 12),
            (-13, 14, -15)
        )

        self.assertEqual(-Matrix_5x3(m), Matrix_5x3(m_negated))

    def test_scalar_division(self):
        m = (
            (1, -2, pi),
            (-4, 5, -(2 * pi)),
            (7, -8, 9),
            (-10, 11, -12.3),
            (13, -14, 15.4321)
        )

        m_division = (
            (1 / 3.25, -2 / 3.25, pi / 3.25),
            (-4 / 3.25, 5 / 3.25, -(2 * pi) / 3.25),
            (7 / 3.25, -8 / 3.25, 9 / 3.25),
            (-10 / 3.25, 11 / 3.25, -12.3 / 3.25),
            (13 / 3.25, -14 / 3.25, 15.4321 / 3.25)
        )

        self.approx_equal(Matrix_5x3(m), Matrix_5x3(m_division))

if __name__ == '__main__':
    unittest.main()
