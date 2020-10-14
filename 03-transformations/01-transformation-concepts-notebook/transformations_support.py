from vectors_my_implementation import add, scale, to_polar, to_cartesian

# Pre-existing
def polygon_map(transformation, polygons):
    return [
        [transformation(vertex) for vertex in polygon]
        for polygon in polygons
    ]

# added on exercise 4.1
def translate_by(vector):
    def new_function(v):
        return add(vector, v)
    return new_function

# added on exercise 4.3
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


# added on exercise 4.6
def compose(*fArgs):
    def new_function(input):
        state = input
        for f in reversed(fArgs):
            state = f(state)
        return state
    return new_function

# added on exercise 4.7
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

