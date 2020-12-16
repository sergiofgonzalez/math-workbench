from my_plot import plot3d
from my_linear_equations import plane_equation


a, b, c, d = plane_equation((1, 1, 1), (3, 0, 0), (0, 3, 0))

def z(x, y):
    return (d - a * x - b * y) / c

plot3d([z], [(1, 1, 1), (3, 0, 0), (0, 3, 0)], [[(3, 3, 3), (1, 1, 1)]], -5, 5,)