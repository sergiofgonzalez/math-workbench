import unittest  # https://docs.python.org/3/library/unittest.html
from math import isclose
from random import uniform
from vector_matrix import Matrix
from test_vector import VectorTestCase

class MatrixTest(VectorTestCase):

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

        if (not Matrix in v.__class__.mro()) or (not Matrix in w.__class__.mro()):
            return False

        if not(v.rows == w.rows and v.columns == w.columns):
            return False
        
        return all(isclose(item_v, item_w) for item_v, item_w in zip(flatten(v), flatten(w)))
