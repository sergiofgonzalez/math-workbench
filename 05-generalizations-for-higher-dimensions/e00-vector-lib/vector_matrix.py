from vector import Vector
from abc import abstractmethod

class Matrix(Vector):

    @classmethod
    @abstractmethod
    def zero(cls):
        pass

    @property
    @abstractmethod
    def rows(self):
        pass

    @property
    @abstractmethod
    def columns(self):
        pass

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

        if len(items) != self.rows:
            raise TypeError('Matrix constructor found an unexpected number of rows')

        if len(items[0]) != self.columns:
            raise TypeError('Matrix constructor found an unexpected number of columns')

        self.items = items

    def add(self, other):
        matrix_sum_as_tuple_of_tuples = tuple(
            tuple(
                self.items[i][j] + other.items[i][j]
                for j in range(0, self.columns))
            for i in range(0, self.rows)
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
