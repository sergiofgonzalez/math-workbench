import unittest  # https://docs.python.org/3/library/unittest.html
from math import isclose, pi
from test_vector import VectorTestCase
from linear_map_3d_to_5d import LinearMap_3d_to_5d
from vector_matrix_2x2 import Matrix_2x2
from vector3d import Vec3
from vector5d import Vec5

class LinearMap_3d_to_5d_TestCase(VectorTestCase):
    def random_items(self, rows, columns):
        if not isinstance(rows, int):
            raise TypeError('random_items expects an int as rows argument')
        if not isinstance(columns, int):
            raise TypeError('random_items expects an int as columns argument')
        
        if (rows < 0 or columns < 0):
            raise ValueError('random_items expects a positive int for both rows and columns arguments')

        items = tuple(
            tuple(self.random_scalar() for _ in range(0, columns))
            for _ in range(0, rows)
        )
        return items

    def approx_equal(self, v, w):
        def flatten(matrix):
            return [item for row in matrix.items for item in row]

        if (not LinearMap_3d_to_5d in v.__class__.mro()) or (not LinearMap_3d_to_5d in w.__class__.mro()):
            return False

        if not(v.source_dimension == w.source_dimension and v.target_dimension == w.target_dimension):
            return False
        
        return all(isclose(item_v, item_w) for item_v, item_w in zip(flatten(v), flatten(w)))

    def test_incorrect_linear_map_cannot_be_built(self):
        with self.assertRaises(TypeError, msg='should raise TypeError when passing incorrect items'):
            LinearMap_3d_to_5d(self.random_items(rows=5, columns=5))

    def test_add_happy_path(self):
        u = LinearMap_3d_to_5d((
            (1, 2, 3),
            (4, 5, 6),
            (7, 8, 9),
            (10, 11, 12),
            (13, 14, 15)
            ))
        
        v = LinearMap_3d_to_5d((
            (16, 17, 18),
            (19, 20, 21),
            (22, 23, 24),
            (25, 26, 27),
            (28, 29, 30)
            ))

        sum_matrix = u + v

        self.assertEqual(sum_matrix, LinearMap_3d_to_5d((
            (17, 19, 21), 
            (23, 25, 27),
            (29, 31, 33),
            (35, 37, 39),
            (41, 43, 45)
            ))
        )

    def test_scalar_product_happy_path(self):
        u = LinearMap_3d_to_5d((
            (1, 2, 3),
            (4, 5, 6),
            (7, 8, 9),
            (10, 11, 12),
            (13, 14, 15)
            ))

        scalar = 2
        scalar_product_matrix = scalar * u

        self.assertTrue(scalar_product_matrix, LinearMap_3d_to_5d((
            (2, 4, 6),
            (8, 10, 12),
            (14, 16, 18),
            (20, 22, 24),
            (26, 28, 30)
            )
        ))

    def test_scalar_rmult_args(self):
        with self.assertRaises(TypeError, msg='should raise TypeError when passing numeric scalar'):
            u = LinearMap_3d_to_5d(self.random_items(rows=5, columns=3))
            s = 'a'
            s * u

    def test_scalar_mult_args(self):
        with self.assertRaises(TypeError, msg='should raise TypeError when passing numeric scalar'):
            u = LinearMap_3d_to_5d(self.random_items(rows=5, columns=3))
            s = 'a'
            u * s

    def test_add_incompatible_types(self):
        with self.assertRaises(TypeError, msg='should raise TypeError when not compatible class'):        
            u = LinearMap_3d_to_5d(self.random_items(rows=5, columns=3))
            v = 1
            u + v

    def test_add_incompatible_subclasses(self):
        with self.assertRaises(TypeError, msg='should raise TypeError when not compatible subclasses'):        
            u = LinearMap_3d_to_5d(self.random_items(rows=5, columns=3))
            v = Matrix_2x2(self.random_items(rows=2, columns=2))
            u + v

    def test_mult_incompatible_types(self):
        class A():
            def sayHello(self):
                return 'hello'

        with self.assertRaises(TypeError, msg='should raise TypeError when not compatible class'):        
            u = LinearMap_3d_to_5d(self.random_items(rows=5, columns=3))
            v = A()
            u + v

    def test_sub_incompatible_types(self):
        with self.assertRaises(TypeError, msg='should raise TypeError when not compatible class'):        
            u = LinearMap_3d_to_5d(self.random_items(rows=5, columns=3))
            v = 'v'
            u - v

    def test_LinearMap_3d_to_5d_is_vector_space(self):
        for _ in range(0, 100):
            a, b = self.random_scalar(), self.random_scalar()
            u, v, w = LinearMap_3d_to_5d(self.random_items(rows=5, columns=3)), LinearMap_3d_to_5d(self.random_items(rows=5, columns=3)), LinearMap_3d_to_5d(self.random_items(rows=5, columns=3))
            self.check_vector_space_rules(self.approx_equal, a, b, u, v, w)

    def test_zero_vector(self):
        self.assertEqual(LinearMap_3d_to_5d.zero(), LinearMap_3d_to_5d(((0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0))))

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

        self.assertEqual(-LinearMap_3d_to_5d(m), LinearMap_3d_to_5d(m_negated))

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

        self.approx_equal(m, m_division)     

    def test_call_happy_path(self):
        linear_map = LinearMap_3d_to_5d((
            (1, 2, 3),
            (4, 5, 6),
            (7, 8, 9),
            (10, 11, 12),
            (13, 14, 15)
        ))

        v3d = Vec3(1, 1, 1)

        expected_result = Vec5(6, 15, 24, 33, 42)

        self.assertEqual(linear_map(v3d), expected_result)


if __name__ == '__main__':
    unittest.main()
