# A collection of vector related functions
# Changelog (most recent first):
# + Added safeguards to vector functions to ensure that operations fail when given
#   incorrect inputs (like vectors of different sizes, etc.)
#

from math import sqrt, pi, acos, sin, cos, atan2


def add(*vectors):
    """Return vector sum resulting of adding the given vectors

    The vectors must be given in their Cartesian coordinates.
    """

    if len(vectors) < 2:
        # according to https://docs.python.org/3/library/exceptions.html#TypeError
        raise TypeError('add requires at least two vectors')

    if not are_vectors_of_same_size(*vectors):
        raise ValueError('add expects vectors to be of the same size')

    if not are_vector_elements_numeric(*vectors):
        raise TypeError('add expects vector elements to be numeric')

    by_coordinate_list = zip(*vectors)
    sum_by_coordinate_list = [sum(coords) for coords in by_coordinate_list]
    return tuple(sum_by_coordinate_list)


def subtract(v, w):
    """Return the vector resulting from subtracting w from v

    The vectors must be given in their Cartesian coordinates.
    """
    if not are_vectors_of_same_size(v, w):
        raise ValueError('subtract expects vectors to be of the same size')

    if not are_vector_elements_numeric(v, w):
        raise TypeError('subtract expects vector elements to be numeric')

    return tuple(v[i] - w[i] for i in range(0, len(v)))


def length(v):
    """Return the length of the vector

    v is a vector given in their Cartesian coordinates.
    """
    if not are_vector_elements_numeric(v):
        raise TypeError('length expects vector elements to be numeric')

    return sqrt(sum([v_i ** 2 for v_i in v]))


def dot(u, v):
    """Return the dot product of u with v

    u and v are vectors of any dimension given in their Cartesian coordinates.
    """
    if not are_vectors_of_same_size(u, v):
        raise ValueError('add expects vectors to be of the same size')

    if not are_vector_elements_numeric(u, v):
        raise TypeError('add expects vector elements to be numeric')

    return sum([coord1 * coord2 for coord1, coord2 in zip(u, v)])


def distance(v1, v2):
    """Return the distance between the given vectors

    The vectors must be given in their Cartesian coordinates.
    """
    if not are_vectors_of_same_size(v1, v2):
        raise ValueError('subtract expects vectors to be of the same size')

    if not are_vector_elements_numeric(v1, v2):
        raise TypeError('subtract expects vector elements to be numeric')

    return length(subtract(v2, v1))


def perimeter(vectors):
    """Return the perimeter of the polygon identified by the given vectors

    The vectors must be given in their Cartesian coordinates.
    """
    if len(vectors) < 3:
        # according to https://docs.python.org/3/library/exceptions.html#TypeError
        raise TypeError('perimeter requires at least three points identifying a polygon')

    if not are_vectors_of_same_size(*vectors):
        raise ValueError('perimeter expects vectors to be of the same size')

    if not are_vector_elements_numeric(*vectors):
        raise TypeError('perimeter expects vector elements to be numeric')

    distances = [distance(vectors[i], vectors[(i + 1) % len(vectors)])
                 for i in range(0, len(vectors))]
    return sum(distances)


def scale(factor, v):
    """Return the vector resulting from scaling the input vector by the given factor.

    Factor is any real number, and v is a vector given in their Cartesian coordinates.
    Effectively, scale relies on the scalar_product.
    """
    if (not isinstance(factor, (int, float))):
        raise TypeError('scale expects factor to be numeric')

    if not are_vector_elements_numeric(v):
        raise TypeError('scale expects vector elements to be numeric')

    return tuple(factor * coord for coord in v)


def to_cartesian(polar_vector):
    """Return the Cartesian coordinates of the given vector

    The given vector must be specified using polar coordinates
    """
    if len(polar_vector) != 2:
        raise TypeError('to_cartesian requires a polar vector with two coordinates')

    if not are_vector_elements_numeric(polar_vector):
        raise TypeError('to_cartesian expects vector elements to be numeric')

    length, angle = polar_vector[0], polar_vector[1]  # this is like destructuring
    return (length * cos(angle), length * sin(angle))


def translate(translation_vector, vectors):
    """Returns the vectors translated according to the given translation vector

    The translation vector and the vectors must be given in their Cartesian coordinates.
    """
    if not are_vectors_of_same_size(translation_vector, *vectors):
        raise ValueError('translate expects vectors to be of the same size')

    if not are_vector_elements_numeric(translation_vector, *vectors):
        raise TypeError('translate expects vector elements to be numeric')

    return [add(translation_vector, v) for v in vectors]


def rotate2d(rotation_angle, vector):
    """Return the vector that results from rotating the given vector by the provided angle

    The rotation angle must be given in radians, and the vector must be a 2D vector
    specified using its Cartesian coordinates
    """
    if (not isinstance(rotation_angle, (int, float))):
        raise TypeError('scale expects factor to be numeric')

    if len(vector) != 2:
        raise TypeError('rotate2d requires a 2D vector')

    if not are_vector_elements_numeric(vector):
        raise TypeError('to_cartesian expects vector elements to be numeric')

    vector_length, vector_angle = to_polar(vector)
    new_vector_angle = vector_angle + rotation_angle
    return to_cartesian((vector_length, new_vector_angle))


def rotate2d_multiple(rotation_angle, vectors):
    """Return the list of vectors rotated by the given angle

    The rotation angle must be given in radians, and the vectors must be 2D vectors
    specified using their Cartesian coordinates
    """
    if (not isinstance(rotation_angle, (int, float))):
        raise TypeError('rotate2d_multiple expects angle to be numeric')

    if len(vectors) < 1:
        raise TypeError('rotate2d_multiple requires at least one vector in the list')

    if not are_all_vectors_of_dimension(*vectors, dimension=2):
        raise ValueError('rotate2d_multiple expects 2D vectors')

    if not are_vector_elements_numeric(*vectors):
        raise TypeError('rotate2d_multiple expects vector elements to be numeric')

    vectors_polar = [to_polar(v) for v in vectors]
    rotated_vectors_polar = [(v[0], v[1] + rotation_angle)
                             for v in vectors_polar]
    rotated_vectors = [to_cartesian(v) for v in rotated_vectors_polar]
    return rotated_vectors


def to_polar(vector):
    """Return the polar coordinates of the given vector

    The given vector must be given in Cartesian coordinates
    """
    if len(vector) != 2:
        raise TypeError('to_polar requires a 2D vector')

    if not are_vector_elements_numeric(vector):
        raise TypeError('to_polar expects vector elements to be numeric')

    x, y = vector[0], vector[1]  # destructuring
    angle = atan2(y, x)
    return (length(vector), angle)


def angle_between(u, v):
    """Return the angle between u and v

    u and v are vectors of any dimension given in their Cartesian coordinates.
    """
    if not are_vectors_of_same_size(u, v):
        raise ValueError('angle_between expects vectors to be of the same size')

    if not are_vector_elements_numeric(u, v):
        raise TypeError('angle_between expects vector elements to be numeric')

    return acos(dot(u, v) / (length(u) * length(v)))


def cross(u, v):
    """Return the cross product of u and v

    The vectors must be 3D vectors given in their Cartesian coordinates
    """
    if not are_all_vectors_of_dimension(u, v, dimension=3):
        raise ValueError('cross expects 3D vectors')

    if not are_vector_elements_numeric(u, v):
        raise TypeError('cross expects vector elements to be numeric')

    ux, uy, uz = u
    vx, vy, vz = v
    return (uy * vz - uz * vy, uz * vx - ux * vz, ux * vy - uy * vx)


def to_radians(degrees):
    """Return the radians value for the given value in degrees"""
    if (not isinstance(degrees, (int, float))):
        raise TypeError('to_radians expects numeric argument')

    return (degrees * pi) / 180


def to_degrees(radians):
    """Return degrees value for the given value in radians"""
    if (not isinstance(radians, (int, float))):
        raise TypeError('to_radians expects numeric argument')

    return (radians * 180) / pi


def component(v, direction):
    """Return the component of v in the given direction.

    The vector and the direction must be given in their Cartesian coordinates
    For example `component((1, 2, 3), (0, 0, 1)) => 3`
    """
    if not are_vectors_of_same_size(v, direction):
        raise ValueError('component expects vectors to be of the same size')

    if not are_vector_elements_numeric(v, direction):
        raise TypeError('angle_between expects vector elements to be numeric')
    return (dot(v, direction) / length(direction))


def unit(v):
    """Return a vector on the same direction as the one given, but with length equal to one

    The vector must be given in its Cartesian coordinates.
    """
    if not are_vector_elements_numeric(v):
        raise TypeError('unit expects vector to be numeric')
    return scale(1. / length(v), v)

# added in exercise 5.1


def standard_basis(dimension):
    """Return an iterable with the vectors of the standard basis for the given dimension

    The dimension given should be a positive integer value
    """
    def standard_basis_vector(i):
        return tuple(1 if i == j else 0 for j in range(0, dimension))

    if not isinstance(dimension, int):
        raise TypeError('standard_basis expects an integer as dimension')

    if dimension < 2:
        raise ValueError('standard_basis expects a positive integer')

    standard_basis = [standard_basis_vector(i) for i in range(0, dimension)]
    return standard_basis

# safeguards and common validations
# added in exercise 5.15


def are_vectors_of_same_size(*vectors):
    if (len(vectors) < 2):
        raise TypeError('are_vectors_of_same_size requires at least 2 vectors')

    expected_size = len(vectors[0])

    all_same_size = all(len(vector) == expected_size for vector in vectors)
    return all_same_size

def are_all_vectors_of_dimension(*vectors, dimension):
    if (len(vectors) < 2):
        raise TypeError('are_all_vectors_of_dimension requires at least 2 vectors')

    if (not isinstance(dimension, int)):
        raise TypeError('are_all_vectors_of_dimension exxpects dimension to be an int')

    all_same_size = all(len(vector) == dimension for vector in vectors)
    return all_same_size

def are_vector_elements_numeric(*vectors):
    def is_vector_element_numeric(elem):
        return isinstance(elem, (int, float))

    are_all_numeric = all(is_vector_element_numeric(elem) for vector in vectors for elem in vector)
    return are_all_numeric