import matplotlib
from vector_arithmetic import subtract, scale, length, dot_product, cross_product
from draw2d import draw2d, Polygon2D



def component(v, direction):
    return (dot_product(v, direction) / length(direction))

def vector_to_2d(v):
    return (component(v, (1, 0, 0)), component(v, (0, 1, 0)))

def face_to_2d(face):
    return [vector_to_2d(vertex) for vertex in face]

blues = matplotlib.cm.get_cmap('Blues')

def unit(v):
    return scale(1. / length(v), v)

def normal(face):
    return (cross_product(subtract(face[1], face[0]), subtract(face[2], face[0])))

def render(faces, light=(1, 2, 3), color_map=blues, lines=None):
    polygons = []
    for face in faces:
        unit_normal = unit(normal(face))
        if unit_normal[2] > 0:
            c = color_map(1 - dot_product(unit(normal(face)), unit(light)))
            p = Polygon2D(*face_to_2d(face), fill=c, color=lines)
            polygons.append(p)
    draw2d(*polygons, axes=False, origin=False, grid=None)