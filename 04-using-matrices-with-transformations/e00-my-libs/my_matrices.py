# from my_transformations import linear_combination # no longer needed
# also: it was creating a circular dependency between transformations and matrices
from my_vectors import dot, standard_basis
from random import randint

# def multiply_matrix_vector(matrix, vector):
#     return linear_combination(vector, *zip(*matrix))

# added in exercise 5.8 (nothing wrong with previous impl, but this one sooo much clear! )
def multiply_matrix_vector(m, v):
    return tuple(dot(row, v) for row in m)

def matrix_multiply(a, b):
    return tuple(
        tuple(dot(row_from_a, col_from_b) for col_from_b in zip(*b))
        for row_from_a in a
    )

# added in exercise 5.1
def infer_matrix(n, transformation):
    """Return the matrix associated to a given transformation function `f(v)`

    Given a transformation function that takes in a vector and returns a transformation
    vector, this function computes the associated transformation matrix that results
    from applying that transformation to the standard basis vectors.
    """
    transformations_on_standard_basis = [transformation(ei) for ei in standard_basis(n)]
    return tuple(zip(*transformations_on_standard_basis))

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

