"""
my_vector_drawing_lib

Annotated implementation of the vector_drawing library.
"""

from math import sqrt, ceil, floor
import matplotlib
import matplotlib.patches
import numpy as np
from matplotlib.pyplot import xlim, ylim
import matplotlib.pyplot as plt

#
# a few named colors we'll use along the way
#
BLUE = 'C0'
BLACK = 'k'
RED = 'C3'
GREEN = 'C2'
PURPLE = 'C4'
ORANGE = 'C1'
GRAY = 'gray'

#
# Class definitions for the *shapes*: Polygon, Points, Arrow and Segment
#



class Polygon():
    """
    Represents a polygon as a 2D object with a variable number of points
    """
    def __init__(self, *vertices, color=BLUE, fill=None, alpha=0.4):
        self.vertices = vertices
        self.color = color
        self.fill = fill
        self.alpha = alpha



class Points():
    """
    Represents a variable number of 2D points in the plane
    """
    def __init__(self, *vectors, color=BLACK):
        self.vectors = list(vectors)
        self.color = color


class Arrow():
    """
    Represents an arrow with 2D points, the tip of the arrow and (optionally)
    its tail.
    If not given, the tail is the origin (0, 0)
    """
    def __init__(self, tip, tail=(0, 0), color=RED):
        self.tip = tip
        self.tail = tail
        self.color = color


class Segment():
    """
    Represent a segment in the 2D plane with two points
    """
    def __init__(self, start_point, end_point, color=BLUE):
        self.start_point = start_point
        self.end_point = end_point
        self.color = color


def extract_vectors(objects):
    """
    A polymorphic generator function that returns the vectors from a list
    of objects iteratively.
    """
    for object_elem in objects:
        if isinstance(object_elem, Polygon):
            for vertex in object_elem.vertices:
                yield vertex
        elif isinstance(object_elem, Points):
            for vertex in object_elem.vectors:
                yield vertex
        elif isinstance(object_elem, Arrow):
            yield object_elem.tip
            yield object_elem.tail
        elif isinstance(object_elem, Segment):
            yield object_elem.start_point
            yield object_elem.end_point
        else:
            raise TypeError(
                f'Unrecognized object {object_elem} of type {type(object_elem)}')


def draw(*objects, origin=True, axes=True, grid=(1, 1), nice_aspect_ratio=True, width=6, save_as=None):
    """
    The main function of the vector drawing library

    It receives a variable number of 2D objects and some additional optional
    parameters and renders them on the screen using matplotlib
    """

    # first we get all the points of the different 2D objects passed
    all_vectors = list(extract_vectors(objects))

    # now we zip them and unpack them into two separate lists for the x's and
    # y's coordinate
    #
    # e.g.:
    # all_vectors = [(1, 2), (3, 4)]
    # zip(*all_vectors) = [(1, 3), (2, 4)]
    # xs, ys = zip(*all_vectors) => xs=(1, 3); ys = (2, 4)
    #
    # also remember that '*' is used to convert a list into something that
    # can be sent to a function that accepts a variable number of arguments
    xs, ys = zip(*all_vectors)

    # calculate max and min in each axis for proper dimensioning
    max_x, max_y, min_x, min_y = max(
        0, *xs), max(0, *ys), min(0, *xs), min(0, *ys)

    if grid:
        x_padding = max(ceil(0.05 * (max_x - min_x)), grid[0])
        y_padding = max(ceil(0.05 * (max_y - min_y)), grid[1])

        plt.xlim(
            floor((min_x - x_padding) / grid[0]) * grid[0],
            ceil((max_x + x_padding) / grid[0]) * grid[0]
        )

        plt.ylim(
            floor((min_y - y_padding) / grid[1]) * grid[1],
            ceil((max_y + y_padding) / grid[1]) * grid[1]
        )

        plt.gca().set_xticks(np.arange(plt.xlim()[0], plt.xlim()[1], grid[0]))
        plt.gca().set_yticks(np.arange(plt.ylim()[0], plt.ylim()[1], grid[1]))
        plt.grid(True)
        plt.gca().set_axisbelow(True)

    if origin:
        # set origin of axis at (0, 0) in black with an x
        plt.scatter([0], [0], color='k', marker='x')

    if axes:
        plt.gca().axhline(linewidth=2, color='k')
        plt.gca().axvline(linewidth=2, color='k')

    for object_elem in objects:
        if isinstance(object_elem, Polygon):
            for i in range(0, len(object_elem.vertices)):
                x1, y1 = object_elem.vertices[i]
                x2, y2 = object_elem.vertices[(i + 1) % len(object_elem.vertices)]
                plt.plot([x1, x2], [y1, y2], color=object_elem.color)
            if object_elem.fill:
                xs = [v[0] for v in object_elem.vertices]
                ys = [v[1] for v in object_elem.vertices]
                plt.gca().fill(xs, ys, object_elem.fill, alpha=object_elem.alpha)
        elif isinstance(object_elem, Points):
            xs = [v[0] for v in object_elem.vectors]
            ys = [v[1] for v in object_elem.vectors]
            plt.scatter(xs, ys, color=object_elem.color)
        elif isinstance(object_elem, Arrow):
            tip, tail = object_elem.tip, object_elem.tail
            tip_length = (xlim()[1] - xlim()[0]) / 20.0
            length = sqrt((tip[1] - tail[1]) ** 2 + (tip[0] - tail[0]) ** 2)
            new_length = length - tip_length
            new_y = (tip[1] - tail[1]) * (new_length / length)
            new_x = (tip[0] - tail[0]) * (new_length / length)
            plt.gca().arrow(tail[0], tail[1], new_x, new_y, head_width=tip_length /
                            1.5, head_length=tip_length, fc=object_elem.color, ec=object_elem.color)
        elif isinstance(object_elem, Segment):
            x1, y1 = object_elem.start_point
            x2, y2 = object_elem.end_point
            plt.plot([x1, x2], [y1, y2], color=object_elem.color)
        else:
            raise TypeError(
                f'Unrecognized object {object_elem} of type {type(object_elem)}')

    fig = matplotlib.pyplot.gcf()

    if nice_aspect_ratio:
        coords_height = (ylim()[1] - ylim()[0])
        coords_width = (xlim()[1] - xlim()[0])
        fig.set_size_inches(width, width * coords_height / coords_width)

    if save_as:
        plt.savefig(save_as)

    # finally, show all the work we've done above!
    plt.show()
