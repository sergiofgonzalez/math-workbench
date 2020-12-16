from my_plot import plot3d

def f(x, y):
    return 3 - x - y

point = (1, 1, 1)

plot3d([f], [point], -5, 5, -5, 5, 'A Plane')