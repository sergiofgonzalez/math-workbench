import unittest  # https://docs.python.org/3/library/unittest.html
from my_vectors import add


# problems tipically arise with zip operations


class MyVectorsTestCase(unittest.TestCase):
    def test_add_no_args(self):
        with self.assertRaises(TypeError, msg='shoud raise TypeError when passing no args'):
            add()

    def test_add_single_vector(self):
        u = (1, 2)
        with self.assertRaises(TypeError, msg='should raise TypeError when passing only one vector'):
            add(u)

    def test_add_2_different_sizes(self):
        u = (1, 2)
        v = (1, 2, 3)
        with self.assertRaises(ValueError, msg='should raise ValueError when passing two vectors of different sizes'):
            add(u, v)

    def test_add_3_different_sizes(self):
        u = (1, 2)
        v = (3, 4)
        w = (5, 6, 7)
        with self.assertRaises(ValueError, msg='should raise ValueError when passing one vector that does not match other vector sizes'):
            add(u, v, w)

    def test_add_vectors_holding_other_than_numbers(self):
        u = ('a', 'b')
        v = ('c', 'd')
        with self.assertRaises(TypeError, msg='should raise TypeError when passing vectors holding no numeric values'):
            add(u, v)

    def test_add_2_happy_path(self):
        u = (1, 2)
        v = (3, 4)
        add_actual_result = add(u, v)
        add_expected_result = (u[0] + v[0], u[1] + v[1])
        self.assertEqual(add_actual_result, add_expected_result, 'add 2 vectors of same size should match')

    def test_add_3_happy_path(self):
        u = (1, 2, 3)
        v = (4, 5, 6)
        w = (7, 8, 9)
        add_actual_result = add(u, v, w)
        add_expected_result = (u[0] + v[0] + w[0], u[1] + v[1] + w[1], u[2] + v[2] + w[2])
        self.assertEqual(add_actual_result, add_expected_result, 'add 2 vectors of same size should match')


if __name__ == '__main__':
    unittest.main()
