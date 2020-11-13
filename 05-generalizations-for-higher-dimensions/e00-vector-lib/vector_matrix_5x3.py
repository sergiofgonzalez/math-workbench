from vector_matrix import Matrix
from abc import abstractmethod
from vector5d import Vec5
from vector3d import Vec3
from my_matrices import multiply_matrix_vector

class Matrix_5x3(Matrix):

    @classmethod
    def zero(cls):
        zero_as_tuple_of_tuples = tuple(
            tuple(0 for _ in range(0, 3))
            for _ in range(0, 5)
        )
        return Matrix_5x3(zero_as_tuple_of_tuples)

    @property
    def rows(self):
        return 5

    @property
    def columns(self):
        return 3

    # added in exercise 6.19
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return super().__mul__(other)
        
        if not Vec3 in other.__class__.mro():
            raise TypeError('matrix multiplication expects a compatible vector with {} elements'.format(self.columns))

        if len(other.coordinates) != self.columns:
            raise TypeError('matrix multiplication expects a compatible vector with {} elements'.format(self.columns))

        resulting_coordinates = multiply_matrix_vector(self.items, other.coordinates)

        return Vec5(*resulting_coordinates)
