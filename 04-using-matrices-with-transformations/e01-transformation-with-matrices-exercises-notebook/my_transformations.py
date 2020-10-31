from my_vectors import add, scale, to_polar, to_cartesian
from my_matrices import multiply_matrix_vector

# Pre-existing
def polygon_map(transformation, polygons):
    return [
        [transformation(vertex) for vertex in polygon]
        for polygon in polygons
    ]

# added in exercise 4.1
def translate_by(vector):
    def new_function(v):
        return add(vector, v)
    return new_function

# added in exercise 4.3
def scale_by(factor):
    def new_function(v):
        return scale(factor, v)
    return new_function

# added on exercise 4.4
# superseded by compose(*fArgs) on exercise 4.6
# def compose(f_last, f_first):
#     def new_function(input):
#         return f_last(f_first(input))
#     return new_function


# added in exercise 4.6
def compose(*fArgs):
    def new_function(input):
        state = input
        for f in reversed(fArgs):
            state = f(state)
        return state
    return new_function

# added in exercise 4.7
def rotate_x_by(angle):
    def new_function(v):
        x, y, z = v
        vector_length, vector_angle = to_polar((y, z))
        new_vector_angle = vector_angle + angle
        new_y, new_z = to_cartesian((vector_length, new_vector_angle))
        return (x, new_y, new_z)
    return new_function


def rotate_y_by(angle):
    def new_function(v):
        x, y, z = v
        vector_length, vector_angle = to_polar((x, z))
        new_vector_angle = vector_angle + angle
        new_x, new_z = to_cartesian((vector_length, new_vector_angle))
        return (new_x, y, new_z)
    return new_function

def rotate_z_by(angle):
    def new_function(v):
        x, y, z = v
        vector_length, vector_angle = to_polar((x, y))
        new_vector_angle = vector_angle + angle
        new_x, new_y = to_cartesian((vector_length, new_vector_angle))
        return (new_x, new_y, z)
    return new_function

# added in chapter 4
def linear_combination(scalars, *vectors):
    scaled = [scale(s, v) for s,v in zip(scalars, vectors)]
    return add(*scaled)

# added in exercise 5.6
def apply_matrix_transformation(matrix):
    """Return the transformation function of the given matrix

    Given a transformation matrix, it returns a function that computes the corresponding
    transformation when applied to a vector. That function can be injected into `polygon_map(...)`
    to draw a transformed 3D model.
    """
    def new_function(v):
        return multiply_matrix_vector(matrix, v)
    return new_function

# added in section 5.3.4
def translate_2d(translation_vector):
    def new_function(v):
        a, b = translation_vector
        x, y = v
        matrix = (
            (1, 0, a),
            (0, 1, b),
            (0, 0, 1)
        )
        upgraded_vector = (x, y, 1)
        x_out, y_out, _ = multiply_matrix_vector(matrix, upgraded_vector)
        return (x_out, y_out)
    return new_function

def translate_3d(translation_vector):
    def new_function(target):
        a, b, c = translation_vector
        x, y, z = target
        matrix = (
            (1, 0, 0, a),
            (0, 1, 0, b),
            (0, 0, 1, c),
            (0, 0, 0, 1)
        )
        vector = (x, y, z, 1)
        x_out, y_out, z_out, _ = \
            multiply_matrix_vector(matrix, vector)
        return (x_out, y_out, z_out)
    return new_function