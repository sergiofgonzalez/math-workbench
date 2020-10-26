import unittest  # https://docs.python.org/3/library/unittest.html
from my_matrices import are_valid_vectors, are_valid_matrices, multiply_matrix_vector

from math import sqrt, sin, cos, pi


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




    # def test_first_arg_non_matrix(self):
    #     m = ((1, 0, 0),
    #         (0, 1, 0),
    #         (0, 0, 1))
    #     v = (1, 0, 0)
    #     with self.assertRaises(TypeError, msg='should raise TypeError when passing vectors holding no numeric values'):
    #         add(u, v)

    # def test_add_2_happy_path(self):
    #     u = (1, 2)
    #     v = (3, 4)
    #     add_actual_result = add(u, v)
    #     add_expected_result = (u[0] + v[0], u[1] + v[1])
    #     self.assertEqual(add_actual_result, add_expected_result, 'add 2 vectors of same size should match')

    # def test_add_3_happy_path(self):
    #     u = (1, 2, 3)
    #     v = (4, 5, 6)
    #     w = (7, 8, 9)
    #     add_actual_result = add(u, v, w)
    #     add_expected_result = (u[0] + v[0] + w[0], u[1] + v[1] + w[1], u[2] + v[2] + w[2])
    #     self.assertEqual(add_actual_result, add_expected_result, 'add 2 vectors of same size should match')

    # # subtract tests
    # def test_subtract_vectors_different_sizes(self):
    #     u = (1, 2)
    #     v = (1, 2, 3)
    #     with self.assertRaises(ValueError, msg='should raise ValueError when passing two vectors of different sizes'):
    #         subtract(u, v)

    # def test_subtract_vectors_holding_other_than_numbers(self):
    #     u = ('a', 'b')
    #     v = ('c', 'd')
    #     with self.assertRaises(TypeError, msg='should raise TypeError when passing vectors holding no numeric values'):
    #         subtract(u, v)

    # def test_subtract_happy_path(self):
    #     u = (1, 2, 3)
    #     v = (4, 5, 6)
    #     subtract_actual_result = subtract(u, v)
    #     subtract_expected_result = (u[0] - v[0], u[1] - v[1], u[2] - v[2])
    #     self.assertEqual(subtract_actual_result, subtract_expected_result, 'subtract vectors of same size should match')

    # # length tests
    # def test_length_vector_holding_other_than_numbers(self):
    #     u = ('a', 'b')
    #     with self.assertRaises(TypeError, msg='should raise TypeError when passing vectors holding no numeric values'):
    #         length(u)

    # def test_length_happy_path(self):
    #     u = (1.1, 2.2)
    #     length_actual_result = length(u)
    #     length_expected_result = sqrt( 1.1 ** 2 + 2.2 ** 2)
    #     self.assertEqual(length_actual_result, length_expected_result, 'length should match')

    # # dot tests
    # def test_dot_vectors_different_sizes(self):
    #     u = (1, 2)
    #     v = (1, 2, 3)
    #     with self.assertRaises(ValueError, msg='should raise ValueError when passing two vectors of different sizes'):
    #         dot(u, v)

    # def test_dot_vectors_holding_other_than_numbers(self):
    #     u = ('a', 'b')
    #     v = ('c', 'd')
    #     with self.assertRaises(TypeError, msg='should raise TypeError when passing vectors holding no numeric values'):
    #         add(u, v)

    # def test_dot_happy_path(self):
    #     u = (1.2, 3.4)
    #     v = (5.6, 7.8)
    #     dot_actual_result = dot(u, v)
    #     dot_expected_result = u[0] * v[0] + u[1] * v[1]
    #     self.assertEqual(dot_actual_result, dot_expected_result, 'dot product should match')

    # # distance tests
    # def test_distance_vectors_different_sizes(self):
    #     u = (1, 2)
    #     v = (1, 2, 3)
    #     with self.assertRaises(ValueError, msg='should raise ValueError when passing two vectors of different sizes'):
    #         distance(u, v)

    # def test_distance_vectors_holding_other_than_numbers(self):
    #     u = ('a', 'b')
    #     v = ('c', 'd')
    #     with self.assertRaises(TypeError, msg='should raise TypeError when passing vectors holding no numeric values'):
    #         distance(u, v)

    # def test_distance_happy_path(self):
    #     u = (1, 2, 3)
    #     v = (4, 5, 6)
    #     distance_actual_result = distance(u, v)
    #     distance_expected_result = sqrt((u[0] - v[0]) ** 2 + (u[1] - v[1]) ** 2 + (u[2] - v[2]) ** 2)
    #     self.assertEqual(distance_actual_result, distance_expected_result, 'distance vectors of same size should match')

    # # perimeter tests
    # def test_perimeter_single_vector(self):
    #     u = (1, 2)
    #     with self.assertRaises(TypeError, msg='should raise TypeError when passing only one vector'):
    #         perimeter(u)

    # def test_perimeter_two_vectors(self):
    #     u = (1, 2)
    #     v = (3, 4)
    #     with self.assertRaises(TypeError, msg='should raise TypeError when passing only one vector'):
    #         perimeter([u, v])

    # def test_perimeter_vectors_different_sizes(self):
    #     u = (0, 0)
    #     v = (1, 0)
    #     w = (0, 1, 0)
    #     with self.assertRaises(ValueError, msg='should raise ValueError when passing two vectors of different sizes'):
    #         perimeter([u, v, w])

    # def test_perimeter_vectors_holding_other_than_numbers(self):
    #     u = ('a', 'b')
    #     v = ('c', 'd')
    #     w = ('e', 'f')
    #     with self.assertRaises(TypeError, msg='should raise TypeError when passing vectors holding no numeric values'):
    #         perimeter([u, v, w])

    # def test_2d_perimeter_happy_path(self):
    #     v1 = (0, 0)
    #     v2 = (1, 0)
    #     v3 = (0, 1)
    #     perimeter_actual_result = perimeter([v1, v2, v3])
    #     perimeter_expected_result = 1 + sqrt(2) + 1
    #     self.assertEqual(perimeter_actual_result, perimeter_expected_result, 'add 2 vectors of same size should match')

    # def test_3d_perimeter_happy_path(self):
    #     v1 = (0, 0, 1)
    #     v2 = (1, 0, 1)
    #     v3 = (0, 1, 1)
    #     perimeter_actual_result = perimeter([v1, v2, v3])
    #     perimeter_expected_result = 1 + sqrt(2) + 1
    #     self.assertEqual(perimeter_actual_result, perimeter_expected_result, 'add 2 vectors of same size should match')

    # # scale tests
    # def test_scale_factor_arg(self):
    #     factor = (1, 0)
    #     vector = 2.0
    #     with self.assertRaises(TypeError, msg='should raise TypeError when not passing an scalar'):
    #         scale(factor, vector)

    # def test_scale_vector_arg(self):
    #     factor = 1.0
    #     vector = 2.0
    #     with self.assertRaises(TypeError, msg='should raise TypeError when not passing a vector'):
    #         scale(factor, vector)

    # def test_scale_vector_holding_other_than_numbers(self):
    #     factor = 1.0
    #     vector = ('a', 'b')
    #     with self.assertRaises(TypeError, msg='should raise TypeError when passing vectors holding no numeric values'):
    #         scale(factor, vector)

    # def test_2d_scale_happy_path(self):
    #     factor = 1.0
    #     vector = (2, 3)
    #     scale_actual_result = scale(factor, vector)
    #     scale_expected_result = (2, 3)
    #     self.assertEqual(scale_actual_result, scale_expected_result, 'scale in 2D should match')

    # def test_3d_scale_happy_path(self):
    #     vector = (1, 2, 3)
    #     factor = 4.5
    #     scale_actual_result = scale(factor, vector)
    #     scale_expected_result = (vector[0] * factor, vector[1] * factor, vector[2] * factor)
    #     self.assertEqual(scale_actual_result, scale_expected_result, 'scale in 2D should match')

    # # to_cartesian tests
    # def test_to_cartesian_non_polar_vector(self):
    #     v = (1, 0, 0)
    #     with self.assertRaises(TypeError, msg='should raise TypeError when passing non-2d polar vector'):
    #         to_cartesian(v)

    # def test_to_cartesian_non_numeric_vector(self):
    #     v = ('a', 'theta')
    #     with self.assertRaises(TypeError, msg='should raise TypeError when passing non-numeric polar vector'):
    #         to_cartesian(v)

    # def test_to_cartesian_happy_path(self):
    #     v = (2, pi / 6)
    #     to_cartesian_actual_result = to_cartesian(v)
    #     to_cartesian_expected_result = (v[0] * cos(v[1]), v[0] * sin(v[1]))
    #     self.assertEqual(to_cartesian_actual_result, to_cartesian_expected_result, 'to_cartesian should match')

    # # translate tests
    # def test_translate_translation_vector_arg(self):
    #     translation_vector = (1, 0)
    #     vectors = [(1, 0, 0), (1, 1, 0)]
    #     with self.assertRaises(ValueError, msg='should raise TypeError when not passing vectors of same dimension'):
    #         translate(translation_vector, vectors)

    # def test_translate_vectors_arg(self):
    #     translation_vector = (1, 0, 0)
    #     vectors = [(1, 0), (1, 1)]
    #     with self.assertRaises(ValueError, msg='should raise TypeError when not passing vectors of same dimension'):
    #         translate(translation_vector, vectors)

    # def test_translate_vector_holding_other_than_numbers(self):
    #     translation_vector = ('a', 'b')
    #     vectors = [(1, 0), (1, 1)]
    #     with self.assertRaises(TypeError, msg='should raise TypeError when not passing numeric vectors'):
    #         translate(translation_vector, vectors)

    # def test_translate_vectors_holding_other_than_numbers(self):
    #     translation_vector = (1, 0)
    #     vectors = [('a', 'b'), (1, 1)]
    #     with self.assertRaises(TypeError, msg='should raise TypeError when not passing numeric vectors'):
    #         translate(translation_vector, vectors)

    # def test_2d_translate_happy_path(self):
    #     translation_vector = (1, 2)
    #     vectors = [(3, 4), (5, 6)]
    #     translate_actual_result = translate(translation_vector, vectors)
    #     translate_expected_result = [(4, 6), (6, 8)]
    #     self.assertEqual(translate_actual_result, translate_expected_result, 'translate in 2D should match')

    # def test_3d_translate_happy_path(self):
    #     translation_vector = (1, 2, 3)
    #     vectors = [(4, 5, 6), (7, 8, 9)]
    #     translate_actual_result = translate(translation_vector, vectors)
    #     translate_expected_result = [(5, 7, 9), (8, 10, 12)]
    #     self.assertEqual(translate_actual_result, translate_expected_result, 'translate in 3d should match')

    # # rotate2d
    # def test_rotate2d_rotation_arg(self):
    #     angle = 'a'
    #     v = (1, 0)
    #     with self.assertRaises(TypeError, msg='should raise TypeError when not passing numeric angle'):
    #         rotate2d(angle, v)

    # def test_rotate2d_vector_arg_dimension(self):
    #     angle = pi
    #     v = (1, 0, 0)
    #     with self.assertRaises(TypeError, msg='should raise TypeError when not passing 2D vector'):
    #         rotate2d(angle, v)

    # def test_rotate2d_vector_arg_numeric(self):
    #     angle = pi
    #     v = ('a', 'b')
    #     with self.assertRaises(TypeError, msg='should raise TypeError when not passing numeric 2D vector'):
    #         rotate2d(angle, v)

    # def test_rotate2d_happy_path(self):
    #     angle = pi / 2
    #     v = (2, 2)
    #     actual_rotate2d_result = rotate2d(angle, v)
    #     expected_rotate2d_result = (-2, 2)
    #     self.assertAlmostEqual(actual_rotate2d_result[0], expected_rotate2d_result[0], msg='rotate2d x should approximately match')
    #     self.assertAlmostEqual(actual_rotate2d_result[1], expected_rotate2d_result[1], msg='rotate2d y should approximately match')

    # # rotate2d_multiple tests
    # def test_rotate2d_multiple_rotation_arg(self):
    #     angle = 'a'
    #     v = (1, 0)
    #     with self.assertRaises(TypeError, msg='should raise TypeError when not passing numeric angle'):
    #         rotate2d_multiple(angle, [v])

    # def test_rotate2d_multiple_no_vectors(self):
    #     angle = pi
    #     with self.assertRaises(TypeError, msg='should raise TypeError when not passing numeric angle'):
    #         rotate2d_multiple(angle, [])

    # def test_rotate2d_multiple_vector_arg_dimension(self):
    #     angle = pi
    #     v = (1, 0, 0)
    #     with self.assertRaises(TypeError, msg='should raise TypeError when not passing 2D vector'):
    #         rotate2d_multiple(angle, [v])

    # def test_rotate2d_multiple_vector_arg_numeric(self):
    #     angle = pi
    #     v = ('a', 'b')
    #     with self.assertRaises(TypeError, msg='should raise TypeError when not passing numeric 2D vector'):
    #         rotate2d_multiple(angle, [v])

    # def test_rotate2d_multiple_happy_path(self):
    #     angle = pi / 2
    #     vectors = [(1, 0), (2, 2)]
    #     actual_rotate2d_multiple_result = rotate2d_multiple(angle, vectors)
    #     expected_rotate2d_multiple_result = [(0, 1), (-2, 2)]
    #     self.assertAlmostEqual(actual_rotate2d_multiple_result[0][0], expected_rotate2d_multiple_result[0][0], msg='rotate2d x should approximately match for v[0]')
    #     self.assertAlmostEqual(actual_rotate2d_multiple_result[0][1], expected_rotate2d_multiple_result[0][1], msg='rotate2d y should approximately match for v[0]')
    #     self.assertAlmostEqual(actual_rotate2d_multiple_result[1][0], expected_rotate2d_multiple_result[1][0], msg='rotate2d x should approximately match for v[1]')
    #     self.assertAlmostEqual(actual_rotate2d_multiple_result[1][1], expected_rotate2d_multiple_result[1][1], msg='rotate2d x should approximately match for v[1]')

    # # to_polar tests
    # def test_to_polar_non_2d_vector(self):
    #     v = (1, 0, 0)
    #     with self.assertRaises(TypeError, msg='should raise TypeError when passing non-2d polar vector'):
    #         to_polar(v)

    # def test_to_polar_non_numeric_vector(self):
    #     v = ('a', 'theta')
    #     with self.assertRaises(TypeError, msg='should raise TypeError when passing non-numeric polar vector'):
    #         to_polar(v)

    # def test_to_polar_happy_path(self):
    #     v = (1, 1)
    #     to_polar_actual_result = to_polar(v)
    #     to_polar_expected_result = (sqrt(2), pi / 4)
    #     self.assertEqual(to_polar_actual_result, to_polar_expected_result, 'to_cartesian should match')

    # # angle_between tests
    # def test_angle_between_different_sizes(self):
    #     u = (1, 0)
    #     v = (0, 1, 1)
    #     with self.assertRaises(ValueError, msg='should raise TypeError when passing non-numeric polar vector'):
    #         angle_between(u, v)

    # def test_angle_between_no_numeric(self):
    #     u = ('a', 'b')
    #     v = (0, 1, 1)
    #     with self.assertRaises(ValueError, msg='should raise TypeError when passing non-numeric polar vector'):
    #         angle_between(u, v)

    # def test_angle_between_happy_path_2d(self):
    #     u = (1, 1)
    #     v = (-1, 1)
    #     angle_between_actual_result = angle_between(u, v)
    #     angle_between_expected_result = pi / 2
    #     self.assertEqual(angle_between_actual_result, angle_between_expected_result, msg="should match 2D")

    # def test_angle_between_happy_path_3d(self):
    #     u = (1, 1, 0)
    #     v = (-1, 1, 0)
    #     angle_between_actual_result = angle_between(u, v)
    #     angle_between_expected_result = pi / 2
    #     self.assertEqual(angle_between_actual_result, angle_between_expected_result, msg="should match 3D")

    # # cross tests
    # def test_cross_non_3d(self):
    #     u = (1, 0)
    #     v = (1, 1, 0)
    #     with self.assertRaises(ValueError, msg='should raise TypeError when passing non-3d vectors'):
    #         cross(u, v)

    # def test_cross_non_numeric(self):
    #     u = ('a', 'b', 'c')
    #     v = (1, 1, 0)
    #     with self.assertRaises(TypeError, msg='should raise TypeError when passing non-3d vectors'):
    #         cross(u, v)

    # def test_cross_happy_path(self):
    #     u = (1, 2, 3)
    #     v = (4, 5, 6)
    #     cross_actual_result = cross(u, v)
    #     cross_expected_result = (12 - 15, -6 + 12, 5 - 8) # using determinant matrix
    #     self.assertEqual(cross_actual_result, cross_expected_result, msg='cross should match')

    # # to_radians
    # def test_to_radians_non_numeric(self):
    #     angle = 'a'
    #     with self.assertRaises(TypeError, msg='should raise TypeError when passing non-numeric argument'):
    #         to_radians(angle)

    # def test_to_radians_happy_path(self):
    #     angle = 90
    #     actual_to_radians_result = to_radians(angle)
    #     expected_to_radians_result = pi / 2
    #     self.assertAlmostEqual(actual_to_radians_result, expected_to_radians_result, msg="to_radians should match")

    # # to_degrees
    # def test_to_degrees_non_numeric(self):
    #     angle = 'a'
    #     with self.assertRaises(TypeError, msg='should raise TypeError when passing non-numeric argument'):
    #         to_degrees(angle)

    # def test_to_degrees_happy_path(self):
    #     angle = pi / 2
    #     actual_to_degrees_result = to_degrees(angle)
    #     expected_to_degrees_result = 90
    #     self.assertAlmostEqual(actual_to_degrees_result, expected_to_degrees_result, msg="to_radians should match")

    # # test component
    # def test_component_same_dimension(self):
    #     u = (1, 0)
    #     v = (1, 0, 0)
    #     with self.assertRaises(ValueError, msg='should raise ValueError when passing vectors of different dimension'):
    #         component(u, v)

    # def test_component_numeric(self):
    #     u = ('a', 'b')
    #     v = (1, 0, 0)
    #     with self.assertRaises(ValueError, msg='should raise ValueError when passing non-numeric vectors'):
    #         component(u, v)

    # def test_component_happy_path(self):
    #     u = (1, 2, 3)
    #     direction = (0, 1, 0)
    #     actual_component_result = component(u, direction)
    #     expected_component_result = 2
    #     self.assertEqual(actual_component_result, expected_component_result, msg='results of component should match')

    # # unit tests :p
    # def test_unit_non_numeric(self):
    #     u = ('a', 'b')
    #     with self.assertRaises(TypeError, msg='should raise TypeError when sending non-numeric vector'):
    #         unit(u)

    # def test_unit_happy_path(self):
    #     u = (1, 1)
    #     actual_unit_result = unit(u)
    #     expected_unit_result = (u[0] / sqrt(2), u[1] / sqrt(2))
    #     self.assertEqual(actual_unit_result, expected_unit_result, 'unit results should match')

    # # standard basis tests
    # def test_standard_basis_dimension_not_int(self):
    #     with self.assertRaises(TypeError, msg='should raise TypeError when passing non-numeric vectors'):
    #         standard_basis(3.0)

    # def test_dimension_less_than_2(self):
    #     with self.assertRaises(ValueError, msg='should raise TypeError when passing non-numeric vectors'):
    #         standard_basis(1)

    # def test_happy_path_2d(self):
    #     actual_standard_basis_result = standard_basis(2)
    #     expected_standard_basis_result = [(1, 0), (0, 1)]
    #     self.assertEqual(actual_standard_basis_result, expected_standard_basis_result, 'standard_basis should match for 2d')

    # def test_happy_path_3d(self):
    #     actual_standard_basis_result = standard_basis(3)
    #     expected_standard_basis_result = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    #     self.assertEqual(actual_standard_basis_result, expected_standard_basis_result, 'standard_basis should match for 3d')

    # def test_happy_path_4d(self):
    #     actual_standard_basis_result = standard_basis(4)
    #     expected_standard_basis_result = [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]
    #     self.assertEqual(actual_standard_basis_result, expected_standard_basis_result, 'standard_basis should match for 4d')

if __name__ == '__main__':
    unittest.main()
