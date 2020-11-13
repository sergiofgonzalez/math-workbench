from vector_matrix import Matrix
from abc import abstractmethod

class Matrix_2x2(Matrix):

    @classmethod
    def zero(cls):
        zero_as_tuple_of_tuples = tuple(
            tuple(0 for _ in range(0, 2))
            for _ in range(0, 2)
        )
        return Matrix_2x2(zero_as_tuple_of_tuples)

    @property
    def rows(self):
        return 2

    @property
    def columns(self):
        return 2
