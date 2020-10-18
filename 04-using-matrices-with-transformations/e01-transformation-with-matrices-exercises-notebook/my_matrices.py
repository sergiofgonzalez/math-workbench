from my_transformations import linear_combination
from my_vectors import dot
from random import randint

def multiply_matrix_vector(matrix, vector):
    return linear_combination(vector, *zip(*matrix))

def matrix_multiply(a, b):
    return tuple(
        tuple(dot(row_from_a, col_from_b) for col_from_b in zip(*b))
        for row_from_a in a
    )

# added in exercise 5.3
def random_matrix(num_rows, num_cols, min_int_inc=0, max_int_inc=10):
    def get_random_in_range(min_val, max_val):
        def new_function():
            return randint(min_val, max_val + 1)
        return new_function
    rand = get_random_in_range(min_int_inc, max_int_inc)
    result = tuple(
        tuple(rand() for i in range(0, num_cols))
        for j in range(0, num_rows)
    )
    return result