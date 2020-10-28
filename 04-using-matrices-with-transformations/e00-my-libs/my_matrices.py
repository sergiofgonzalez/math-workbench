# from my_transformations import linear_combination # no longer needed
# also: it was creating a circular dependency between transformations and matrices
from my_vectors import dot, standard_basis
from random import randint

# def multiply_matrix_vector(matrix, vector):
#     return linear_combination(vector, *zip(*matrix))

# added in exercise 5.8 (nothing wrong with previous impl, but this one sooo much clear! )
def multiply_matrix_vector(m, v):
    if not are_valid_matrices(m):
        raise TypeError('multiply_matrix_vector requires a valid matrix as first argument')

    if not are_valid_vectors(v):
        raise TypeError('multiply_matrix_vector requires a numeric vector as argument')

    if get_matrix_dimensions(m)['num_cols'] != len(v):
        raise TypeError('multiply_matrix_vector requires matrix num columns to match vector size')

    return tuple(dot(row, v) for row in m)

def matrix_multiply(a, b):
    if not are_valid_matrices(a, b):
        raise TypeError('multiply_matrix_vector requires valid matrices as arguments')

    if get_matrix_dimensions(a)['num_cols'] != get_matrix_dimensions(b)['num_rows']:
        raise TypeError('multiply_matrix_vector requires matrix compatible for multiplication')

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
    if not isinstance(n, int):
        raise TypeError('infer_matrix requires an int as the first argument')

    if n < 2:
        raise ValueError('infer_matrix requires an int greater or equal than 2')

    if not callable(transformation):
        raise TypeError('infer_matrix requires a function taking a vector as second argument')

    transformations_on_standard_basis = [transformation(ei) for ei in standard_basis(n)]
    return tuple(zip(*transformations_on_standard_basis))

# added in exercise 5.3
def random_matrix(num_rows, num_cols, min_int_inc=0, max_int_inc=10):
    def get_random_in_range(min_val, max_val):
        def new_function():
            return randint(min_val, max_val)
        return new_function

    if not isinstance(num_rows, int):
        raise TypeError('random_matrix expects first argument to be an int')

    if not isinstance(num_cols, int):
        raise TypeError('random_matrix expects second argument to be an int')

    if not isinstance(min_int_inc, int):
        raise TypeError('random_matrix expects min_int_inc to be an int')

    if not isinstance(max_int_inc, int):
        raise TypeError('random_matrix expects min_int_inc to be an int')

    if not isinstance(num_rows, int):
        raise TypeError('random_matrix expects first argument to be an int')

    if num_cols < 2:
        raise ValueError('random_matrix expects first argument to be >= 2')

    if num_rows < 2:
        raise ValueError('random_matrix expects second argument to be >= 2')

    rand = get_random_in_range(min_int_inc, max_int_inc)
    result = tuple(
        tuple(rand() for i in range(0, num_cols))
        for j in range(0, num_rows)
    )
    return result

# supporting functions, safeguards and common validations
# added in exercise 5.15

def get_matrix_dimensions(m):
    """Returns a dictionary object with rows and columns

    The function will fail if not passing a valid matrix
    """
    if not are_valid_matrices(m):
        raise TypeError('get_matrix_dimensions requires a valid matrix')

    num_rows = len(m)
    num_cols = len(m[0])

    return {'num_rows': num_rows, 'num_cols': num_cols, 'printable_str': '{}x{}'.format(num_rows, num_cols)}


def are_valid_vectors(*vectors):
    """
    Requirements for a valid vector:
        + a vector is a tuple
        + all elements of the tuple are numeric
    """
    # early detection, otherwise iteration for are_all_numeric will fail
    are_all_tuples = all(isinstance(vector, tuple) for vector in vectors)
    if not are_all_tuples:
        return False

    are_all_numeric = all(isinstance(elem, (int, float)) for vector in vectors for elem in vector)
    return are_all_numeric

def are_valid_matrices(*matrices):
    """
    Requirements for a matrix:
        + a matrix is a tuple of tuples:
            + matrix is a tuple
            + all elements of a matrix are tuples
        + all rows must have same number of elements
        + all elements must be numeric
    """
    def is_matrix(m):
        # checking if m if tuple of tuples, otherwise, further iteration will fail
        m_is_tuple_of_tuples = all(isinstance(row, tuple) for row in m)
        if not m_is_tuple_of_tuples:
            return False

        if len(m) < 1 and len(m[0]) < 1:
            return TypeError('is_matrix expects a matrix with at least one row and one column')

        num_cols = len(m[0])

        return all(len(row) == num_cols and isinstance(elem, (int, float)) for row in m for elem in row)


    are_all_tuples = all(isinstance(m, tuple) for m in matrices)
    if not are_all_tuples:
        return False

    all_matrices = all(is_matrix(m) for m in matrices)
    return all_matrices