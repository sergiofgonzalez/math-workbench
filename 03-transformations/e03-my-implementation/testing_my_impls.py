from teapot import load_triangles
from draw_model_custom_impl import draw_model_anim
from transformations_support import *
from vectors_my_implementation import to_radians


# Basic rendering of Utah teapot, no transformations
#draw_model_anim(load_triangles())

# Rendering of Utah teapot, using non-curried transformation
# orig_triangles = load_triangles()
# scaled_triangles = [
#   [scale(0.5, v) for v in triangle]
#   for triangle in orig_triangles
# ]
# draw_model_anim(scaled_triangles)

# Rendering using currying and polygon_map
# draw_model_anim(polygon_map(translate_by((-1, -1, -1)), load_triangles()))

# Rendering using composition
draw_model_anim(polygon_map(compose(rotate_z_by(to_radians(45)), rotate_y_by(to_radians(45)), rotate_x_by(to_radians(45))), load_triangles()))