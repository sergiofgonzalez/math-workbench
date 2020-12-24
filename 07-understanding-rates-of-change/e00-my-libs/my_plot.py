import numpy as np
import matplotlib.pyplot as plt
from my_linear_equations import secant_line


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
        ax.scatter(x, y, z, color='black')

    for vector in vectors:
        if len(vector) == 3:
            vector = [vector, (0, 0, 0)]

        vector_head, vector_tail = vector
        plt.quiver(
            vector_tail[0], vector_tail[1], vector_tail[2],
            vector_head[0], vector_head[1], vector_head[2]
        )

    plt.show()


# Added in Exercise 8.3
def plot_secant(f, x1, x2, color='k', title=None, xmin=0, xmax=10, ymin=0, ymax=10):
    """Convenience function that plots f(x) along with the secant line between
    the points x1 and x2.
    """
    secant_fn = secant_line(f, x1, x2)

    fig, ax = plt.subplots()

    if title:
        plt.title(title, fontsize=16)

    plt.ylim(ymin, ymax)
    plt.xticks(np.arange(xmin, xmax + 1, step=1))

    # plotting the function
    xs = np.linspace(xmin, xmax, 100)
    plt.plot(xs, [f(x) for x in xs], label='f(x)')

    xs = np.linspace(x1, x2, 100)
    plt.plot(xs, secant_fn(xs), label='secant line from x={} to x={}'.format(x1, x2), color=color)

    # this is just styling
    xs = np.linspace(xmin, x1, 100)
    plt.plot(xs, secant_fn(xs), color=color, linestyle='dashed')
    xs = np.linspace(x2, xmax, 100)
    plt.plot(xs, secant_fn(xs), color=color, linestyle='dashed')
    ys = np.linspace(0, f(x1))
    xs = x1 * np.ones(len(ys))
    plt.plot(xs, ys, color='black', linestyle='dashed')
    ys = np.linspace(0, f(x2))
    xs = x2 * np.ones(len(vs))
    plt.plot(xs, ys, color='black', linestyle='dashed')


    plt.xlabel(r'x')
    plt.ylabel(r'f(x)')
    plt.legend(bbox_to_anchor=(1, 1))
    plt.grid(True)
    plt.show()