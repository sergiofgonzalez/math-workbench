from vector import Vector
from abc import abstractmethod
from vector3d import Vec3
from vector5d import Vec5
from my_matrices import multiply_matrix_vector

class LinearMap_3d_to_5d(Vector):

    @classmethod
    def zero(cls):
        zero_as_tuple_of_tuples = tuple(
            tuple(0 for _ in range(0, 3))
            for _ in range(0, 5)
        )
        return LinearMap_3d_to_5d(zero_as_tuple_of_tuples)

    @property
    def target_dimension(self):
        return 5

    @property
    def source_dimension(self):
        return 3

    def __init__(self, items):
        def is_matrix(m):
            # checking if m if tuple of tuples, otherwise, further iteration will fail
            m_is_tuple_of_tuples = all(isinstance(row, tuple) for row in m)
            if not m_is_tuple_of_tuples:
                return False

            if len(m) < 1 and len(m[0]) < 1:
                return False

            num_cols = len(m[0])
            
            return all(len(row) == num_cols and isinstance(elem, (int, float)) for row in m for elem in row)

        if not is_matrix(items):
            raise TypeError('Matrix constructor expects items to be a well-formed, regular tuple of tuples')

        if len(items) != self.target_dimension:
            raise TypeError('Matrix constructor found an unexpected number of rows')

        if len(items[0]) != self.source_dimension:
            raise TypeError('Matrix constructor found an unexpected number of columns')

        self.items = items

    def add(self, other):
        matrix_sum_as_tuple_of_tuples = tuple(
            tuple(
                self.items[i][j] + other.items[i][j]
                for j in range(0, self.source_dimension))
            for i in range(0, self.target_dimension)
        )
        sum_as_matrix = self.__class__(matrix_sum_as_tuple_of_tuples)
        return sum_as_matrix

    def scale(self, scalar):
        matrix_scalar_product_as_tuple_of_tuples = tuple(
            tuple(scalar * item for item in row)
            for row in self.items
        )
        matrix_scalar_product_as_matrix = self.__class__(matrix_scalar_product_as_tuple_of_tuples)
        return matrix_scalar_product_as_matrix

    def __repr__(self):
        return '{}{}'.format(self.__class__.__qualname__, self.items)

    def __eq__(self, other):
        if not self.__class__ in other.__class__.mro():
            return False
        else:        
            return self.items == other.items

    def __call__(self, v):
        result = multiply_matrix_vector(self.items, v.coordinates)
        return Vec5(*result)

