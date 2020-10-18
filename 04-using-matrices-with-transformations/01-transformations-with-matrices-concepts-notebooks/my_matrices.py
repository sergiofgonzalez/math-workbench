from my_transformations import linear_combination
from my_vectors import dot

def multiply_matrix_vector(matrix, vector):
    return linear_combination(vector, *zip(*matrix))

def matrix_multiply(a, b):
    return tuple(
        tuple(dot(row_from_a, col_from_b) for col_from_b in zip(*b))
        for row_from_a in a
    )