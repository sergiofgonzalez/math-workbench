import unittest  # https://docs.python.org/3/library/unittest.html
from my_matrices import are_valid_vectors, are_valid_matrices, multiply_matrix_vector, matrix_multiply, infer_matrix, random_matrix

from math import sqrt, sin, cos, pi, floor


# Problems tipically arise with zip operations, but for exploration of a few basic Python
# techniques such as exceptions, unit testing and assertions, etc. I have spend more time
# in this.
# Note that happy path tests have been added only for sampling how the different functions
# should be invoked, rather than checking the actual functionality.


class MyMatricesTestCase(unittest.TestCase):

    # test validations first
    def test_are_valid_vectors_no_tuple(self):
        self.assertFalse(are_valid_vectors('a'))
        self.assertFalse(are_valid_vectors(1))
        self.assertFalse(are_valid_vectors(1.2))
        self.assertFalse(are_valid_vectors([1, 2]))

    def test_are_valid_vectors_no_numeric(self):
        self.assertFalse(are_valid_vectors(('a', 1)))
        self.assertFalse(are_valid_vectors((1, 'a')))
        self.assertFalse(are_valid_vectors((1, 2), (1, 'a')))
        self.assertFalse(are_valid_vectors((1, 2), ('a', 1)))

    def test_are_valid_matrices_no_tuple_of_tuples(self):
        elem = 1
        self.assertFalse(are_valid_matrices(elem))

        vector = (1, 0)
        self.assertFalse(are_valid_matrices(vector))


    def test_are_valid_matrices_not_well_formed(self):
        invalid_matrix_1 = (
            (1, 2, 3),
            (4, 5)
        )
        valid_matrix = (
            (1, 2),
            (3, 4)
        )

        self.assertFalse(are_valid_matrices(invalid_matrix_1))
        self.assertFalse(are_valid_matrices(valid_matrix, invalid_matrix_1))
        self.assertFalse(are_valid_matrices(invalid_matrix_1), valid_matrix)

    def test_are_valid_matrices_no_numeric_elems(self):
        invalid_matrix_1 = (
            ('a', 2, 3),
            (4, 5, 6)
        )

        invalid_matrix_2 = (
            (4, 5, 6),
            ('a', 2, 3)
        )

        valid_matrix = (
            (1, 2),
            (3, 4)
        )

        self.assertFalse(are_valid_matrices(invalid_matrix_1))
        self.assertFalse(are_valid_matrices(valid_matrix, invalid_matrix_1))
        self.assertFalse(are_valid_matrices(invalid_matrix_1), valid_matrix)

        self.assertFalse(are_valid_matrices(invalid_matrix_2))
        self.assertFalse(are_valid_matrices(valid_matrix, invalid_matrix_2))
        self.assertFalse(are_valid_matrices(invalid_matrix_2), valid_matrix)


    # multiply_matrix_vector tests
    def test_multiply_matrix_vector_non_valid_sizes_1(self):
        with self.assertRaises(TypeError, msg='should raise TypeError when passing invalid sizes for multiplication'):
            m = (
                (1, 2, 3),
                (4, 5, 6)
            )
            v = (1, 2)
            multiply_matrix_vector(m, v)

    def test_multiply_matrix_vector_non_valid_sizes_2(self):
        with self.assertRaises(TypeError, msg='should raise TypeError when passing invalid sizes for multiplication'):
            m = (
                (1, 2, 3),
                (4, 5, 6)
            )
            v = (1, 2, 3, 4)
            multiply_matrix_vector(m, v)

    def test_multiply_matrix_vector_non_valid_matrix_1(self):
        with self.assertRaises(TypeError, msg='should raise TypeError when passing invalid sizes for multiplication'):
            m = (
                (1, 2, 'a'),
                (4, 5, 6)
            )
            v = (1, 2, 3, 4)
            multiply_matrix_vector(m, v)

    def test_multiply_matrix_vector_non_valid_matrix_2(self):
        with self.assertRaises(TypeError, msg='should raise TypeError when passing not well-formed matrix for multiplication'):
            m = (1, 2, 3)
            v = (1, 2, 3)
            multiply_matrix_vector(m, v)

    def test_multiply_matrix_vector_non_valid_matrix_3(self):
        with self.assertRaises(TypeError, msg='should raise TypeError when passing not well-formed matrix for multiplication'):
            m = (
                (1, 2, 3),
                (4, 5)
            )
            v = (1, 2, 3)
            multiply_matrix_vector(m, v)

    def test_multiply_matrix_vector_non_valid_vector_1(self):
        with self.assertRaises(TypeError, msg='should raise TypeError when passing not valid vector for multiplication'):
            m = (
                (1, 2, 3),
                (4, 5, 6),
                (7, 8, 9)
            )
            v = (1, 'a', 3)
            multiply_matrix_vector(m, v)

    def test_multiply_matrix_vector_non_valid_vector_2(self):
        with self.assertRaises(TypeError, msg='should raise TypeError when passing not valid vector for multiplication'):
            m = (
                (1, 2, 3),
                (4, 5, 6),
                (7, 8, 9)
            )
            v = 1
            multiply_matrix_vector(m, v)

    def test_multiply_matrix_vector_happy_path_2d(self):
        m = (
            (1, 2),
            (3, 4)
        )
        v = (1, 2)
        actual_multiplication_result = multiply_matrix_vector(m, v)
        expected_multiplication_result = (5, 11)

        self.assertEqual(actual_multiplication_result, expected_multiplication_result, msg='multiplication results should match')

    def test_multiply_matrix_vector_happy_path_3d(self):
        m = (
            (1, 2, 3),
            (4, 5, 6),
            (7, 8, 9)
        )
        v = (1, 2, 3)
        actual_multiplication_result = multiply_matrix_vector(m, v)
        expected_multiplication_result = (14, 32, 50)

        self.assertEqual(actual_multiplication_result, expected_multiplication_result, msg='multiplication results should match')

    def test_matrix_multiply_non_valid_matrix_a(self):
        with self.assertRaises(TypeError, msg='should fail when first matrix is not a valid one'):
            a = 1
            b = (
                (1, 2, 3),
                (4, 5, 6)
            )
            matrix_multiply(a, b)

    def test_matrix_multiply_non_valid_matrix_b(self):
        with self.assertRaises(TypeError, msg='should fail when first matrix is not a valid one'):
            a = (
                (1, 2, 3),
                (4, 5, 6)
            )
            b = 1
            matrix_multiply(a, b)

    def test_matrix_multiply_non_valid_matrix_a_non_numeric(self):
        with self.assertRaises(TypeError, msg='should fail when first matrix is not a valid one'):
            a = (
                (1, 2, 3),
                (4, '5', 6)
                )
            b = (
                (7, 8),
                (9, 10),
                (11, 12)
            )
            matrix_multiply(a, b)

    def test_matrix_multiply_non_valid_matrix_b_non_numeric(self):
        with self.assertRaises(TypeError, msg='should fail when first matrix is not a valid one'):
            a = (
                (1, 2, 3),
                (4, 5, 6)
                )
            b = (
                (7, 8),
                ('a', 10),
                (11, 12)
            )
            matrix_multiply(a, b)

    def test_matrix_multiply_non_valid_matrix_sizes(self):
        with self.assertRaises(TypeError, msg='should fail when first matrix is not a valid one'):
            a = (
                (1, 2, 3),
                (4, 5, 6)
            )
            b = (
                (1, 2, 3),
                (4, 5, 6)
            )
            matrix_multiply(a, b)

    def test_matrix_multiply_happy_path_square_matrices(self):
            a = (
                (1, 2),
                (3, 4)
            )
            b = (
                (5, 6),
                (7, 8)
            )
            actual_matrix_multiply_result = matrix_multiply(a, b)
            expected_matrix_multiply_result = (
                (19, 22),
                (43, 50)
                )
            self.assertEqual(actual_matrix_multiply_result, expected_matrix_multiply_result, msg='result should match')

    def test_matrix_multiply_happy_path_non_square_matrices(self):
            a = (
                (1, 2, 3),
                (4, 5, 6)
            )
            b = (
                (5, 6),
                (7, 8),
                (9, 10)
            )
            actual_matrix_multiply_result = matrix_multiply(a, b)
            expected_matrix_multiply_result = (
                (46, 52),
                (109, 124)
                )
            self.assertEqual(actual_matrix_multiply_result, expected_matrix_multiply_result, msg='result should match')

    # infer_matrix tests
    def test_infer_matrix_invalid_dimension(self):
        with self.assertRaises(TypeError, msg='should fail when not giving int'):
            def transformation(v):
                return v

            infer_matrix('a', transformation)

        with self.assertRaises(TypeError, msg='should fail when not giving int'):
            infer_matrix(2.0, transformation)

        with self.assertRaises(ValueError, msg='should fail when not giving int >= 2'):
            infer_matrix(1, transformation)

    def test_infer_matrix_invalid_function(self):
        with self.assertRaises(TypeError, msg='should fail when not giving int'):
            infer_matrix(2, 'a')

    def test_infer_matrix_happy_path(self):
        def transformation(v):
            return v

        actual_infer_matrix = infer_matrix(3, transformation)
        expected_infer_matrix = (
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1))
        self.assertEqual(actual_infer_matrix, expected_infer_matrix, msg='results should match')

    # random_matrix tests
    def test_random_matrix_invalid_args(self):
        with self.assertRaises(TypeError, msg='should fail when passing invalid num_rows'):
            random_matrix('a', 2)

        with self.assertRaises(TypeError, msg='should fail when passing invalid num_cols'):
            random_matrix(2, 'dos')

        with self.assertRaises(TypeError, msg='should fail when passing invalid min_int_inc'):
            random_matrix(2, 2, min_int_inc='a')

        with self.assertRaises(TypeError, msg='should fail when passing invalid max_int_inc'):
            random_matrix(2, 2, max_int_inc='a')

        with self.assertRaises(ValueError, msg='should fail when passing num_rows < 2'):
            random_matrix(1, 2)

        with self.assertRaises(ValueError, msg='should fail when passing num_cols < 2'):
            random_matrix(2, 1)

    def test_random_matrix_return_proper_dimensions(self):
        actual_random_matrix_result = random_matrix(3, 4)
        expected_num_rows = 3
        expected_num_cols = 4
        self.assertEqual(len(actual_random_matrix_result), expected_num_rows)
        self.assertEqual(len(actual_random_matrix_result[0]), expected_num_cols)
        self.assertEqual(len(actual_random_matrix_result[1]), expected_num_cols)
        self.assertEqual(len(actual_random_matrix_result[2]), expected_num_cols)

    def test_random_matrix_return_proper_elem_values(self):
        num_samples = 1000000

        num_rows = floor(sqrt(num_samples))
        num_cols = floor(sqrt(num_samples))
        actual_random_matrix = random_matrix(num_rows, num_cols)
        min_boundary_reached = False
        max_boundary_reached = False
        for i in range(0, num_rows):
            for j in range(0, num_cols):
                self.assertGreaterEqual(actual_random_matrix[i][j], 0)
                self.assertLessEqual(actual_random_matrix[i][j], 10)
                if not min_boundary_reached and actual_random_matrix[i][j] == 0:
                    min_boundary_reached = True
                if not max_boundary_reached and actual_random_matrix[i][j] == 10:
                    max_boundary_reached = True

        self.assertTrue(min_boundary_reached, 'min boundary should be reached')
        self.assertTrue(max_boundary_reached, 'max boundary should be reached')

    def test_random_matrix_return_proper_elem_values_when_custom_given(self):
        num_samples = 1000000
        min_boundary = -100
        max_boundary = 200

        num_rows = floor(sqrt(num_samples))
        num_cols = floor(sqrt(num_samples))
        actual_random_matrix = random_matrix(num_rows, num_cols, min_boundary, max_boundary)
        min_boundary_reached = False
        max_boundary_reached = False
        for i in range(0, num_rows):
            for j in range(0, num_cols):
                self.assertGreaterEqual(actual_random_matrix[i][j], min_boundary)
                self.assertLessEqual(actual_random_matrix[i][j], max_boundary)
                if not min_boundary_reached and actual_random_matrix[i][j] == min_boundary:
                    min_boundary_reached = True
                if not max_boundary_reached and actual_random_matrix[i][j] == max_boundary:
                    max_boundary_reached = True

        self.assertTrue(min_boundary_reached, 'min boundary should be reached')
        self.assertTrue(max_boundary_reached, 'max boundary should be reached')

if __name__ == '__main__':
    unittest.main()
