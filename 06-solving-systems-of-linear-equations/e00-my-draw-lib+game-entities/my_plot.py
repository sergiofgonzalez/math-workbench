import numpy as np
import matplotlib.pyplot as plt
from my_colors import black

def plot(functions, xmin, xmax, title=None):
    xs = np.linspace(xmin, xmax, 100)
    fig, ax = plt.subplots()
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    if title:
        fig.suptitle(title, fontsize=16)
    for f in functions:
        ys = [f(x) for x in xs]
        plt.plot(xs, ys)

    # this line is not required when running in Jupyter notebook environments
    plt.show()

def plot3d(functions, points, vectors, xmin, xmax, ymin=None, ymax=None):
    """Plots a set of functions and points and vectors in 3D.

    The functions must be given with the z coordinate cleared out in the form:
    z(x, y) = expression involving x and y.

    The vectors can be given as coordinate points when set in the origin as in
    (3, 3, 3)
    or as a set of [head, tail] coordinates, for example [(3, 3, 3), (1, 1, 1)].
    """
    if ymin is None:
        ymin = xmin

    if ymax is None:
        ymax = xmax

    # 0.5 is hardcoded
    x_values = np.arange(xmin, xmax, 0.5)
    y_values = np.arange(ymin, ymax, 0.5)

    xx, yy = np.meshgrid(x_values, y_values)
    plt3d = plt.figure().gca(projection='3d')

    for function in functions:
        plt3d.plot_surface(xx, yy, function(xx, yy), alpha=0.7)

    ax = plt.gca()

    for point in points:
        x, y, z = point
        ax.scatter(x, y, z, color=black)

    for vector in vectors:
        if len(vector) == 3:
            vector = [vector, (0, 0, 0)]

        vector_head, vector_tail = vector
        plt.quiver(
            vector_tail[0], vector_tail[1], vector_tail[2],
            vector_head[0], vector_head[1], vector_head[2]
        )

    plt.show()