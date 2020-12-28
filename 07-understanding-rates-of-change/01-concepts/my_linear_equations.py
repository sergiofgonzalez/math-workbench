from my_vectors import add, scale, subtract, distance, cross, dot
import numpy as np

def standard_form(v1, v2):
    """Return the coefficients of the standard form line
    that passes through the points v1 and v2
    """

    validate_vectors(v1, v2)

    x1, y1 = v1
    x2, y2 = v2
    a = y2 - y1
    b = x1 - x2
    c = x1 * y2 - y1 * x2
    return (a, b, c)

def standard_form_fn(v1, v2):
    """Return the function for the standard form line
    that passes through the points v1 and v2
    """

    validate_vectors(v1, v2)

    a, b, c = standard_form(v1, v2)

    if b == 0:
        raise ValueError('standard_form_fn: divide by zero!')

    def new_function(x):
        return (c - a * x) / b

    return new_function

def parametric_form_fn(v1, v2):
    """Returns the function that corresponds to the parametric
    formula of the line r(t) = u + t v
    """
    def new_function(t):
        return add(v1, scale(t, subtract(v2, v1)))

    return new_function


# Added in exercise 7.19
def plane_equation(p0, p1, p2):
    """Returns the coefficients a, b, c, d for a plane's equation in
    its standard form (ax + by + cz = d) given three points p0, p1, p2
    in the plane
    """
    vector_in_the_plane_1 = subtract(p1, p0)
    vector_in_the_plane_2 = subtract(p2, p0)
    vector_perpendicular_to_the_plane = cross(vector_in_the_plane_1, vector_in_the_plane_2)
    a, b, c = vector_perpendicular_to_the_plane
    d = dot(vector_perpendicular_to_the_plane, p1)

    return a, b, c, d

def intersection(u1, u2, v1, v2):
    """Return the intersection point of the line that goes through
    the points u1 and u2 and the line that goes through v1 and v2.
    All 4 given points are points of the 2D plane in Cartesian
    coordinates.
    """
    a1, b1, c1 = standard_form(u1, u2)
    a2, b2, c2 = standard_form(v1, v2)

    intersection = np.linalg.solve(
        np.array(
            ((a1, b1),
             (a2, b2))
        ),
        np.array(
             (c1, c2)
        )
    )

    return intersection

def do_segments_intersect(s1, s2):
    """Return True if the two segments defined by s1 and s2 intersect,
    or false otherwise.
    s1 and s2 are two sets of points.
    """
    u1, u2 = s1
    v1, v2 = s2
    d1 = distance(u1, u2)
    d2 = distance(v1, v2)
    try:
        x, y = intersection(u1, u2, v1, v2)
        return (
            distance(u1, (x, y)) <= d1 and
            distance(u2, (x, y)) <= d1 and
            distance(v1, (x, y)) <= d2 and
            distance(v2, (x, y)) <= d2
        )

    except np.linalg.LinAlgError:
        return False


def validate_vectors(*vectors):
    """Return True if the given vectors are 2D vectors with numeric
    coordinates.
    """

    if not all([len(vector) == 2] for vector in vectors):
        raise TypeError('validate_vectors require 2D vectors')

    if not all([isinstance(coordinate, (int, float)) for vector in vectors for coordinate in vector]):
        raise TypeError('validate_vectors require vectors with numeric coordinates')


# Added in exercise 8.2
def secant_line(f, x1, x2):
    """Returns the secant line function for a generic function f
    that between the points f(x1) and f(x2)
    """
    def new_function(x):
        return ((f(x2) - f(x1))/(x2 - x1)) * x + (x2 * f(x1) - x1 * f(x2))/(x2 - x1)
    return new_function

def average_rate(f, t1, t2):
    """Returns the average rate of change for the function f between the points t1 and t2.
    That is, this function returns the slope of the secant line between f(t1) and f(t2).
    """
    return (f(t2) - f(t1))/(t2 - t1)

def interval_average_rates(f, t1, t2, dt):
    """Return a series of samples of the average rate (slope of the tangent) function
    between t1 and t2, with each step being dt.
    """
    time_samples = np.arange(t1, t2, dt)
    return [(t, average_rate(f, t, t + dt)) for t in time_samples]

def instantaneous_rate(f, t, digits=6):
    """Returns the instantaneous rate for f at time=t with digits precision
     (that is, the derivative of f at time=t with the given precision)
     Arbitrarily, the convergence will take up to 2*digits iterations on which
     the time interval will be made smaller by 1/10.
     If after those iterations, the derivative does not converge to any value,
     an exception will be raised
     """
    tolerance = 10 ** (-digits)
    h = 1
    approx = average_rate(f, t - h, t + h)
    for _ in range(0, 2 * digits):
        h = h / 10
        next_approx = average_rate(f, t - h, t + h)
        if abs(next_approx - approx) < tolerance:
            return round(next_approx, digits)
        else:
            approx = next_approx
    raise Exception('Derivative did not converge in {} iterations'.format(2 * digits))