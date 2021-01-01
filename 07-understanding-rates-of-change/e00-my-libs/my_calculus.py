import numpy as np

######## Integrals
def small_cumulative_change(rate_fn, t, dt):
    """Returns the value for a small cumulative change (area under a infinitesimal
    interval) given a rate function rate_fn, on a certain point in time t, on
    a small interval dt.

    This function is a building block to calculate the integral of a function.
    """

    return rate_fn(t) * dt

def cumulative_change(rate_fn, t1, t2, dt):
    """Returns the cumulative value (area under the function) given a
    rate function and two points in time t1, t2 and a value for the length
    of the infinitesimal intervals (should be small) dt.

    This function is a building block to calculate the integral of a function.
    """
    return sum(small_cumulative_change(rate_fn, t, dt) for t in np.arange(t1, t2, dt))

def approximate_cumulative_value(rate_fn, v0, dt, T):
    """Returns the approximate cumulative value (area under the function)
    given a rate function, an initial value for the cumulative value v0,
    a value for the length of the infinitesimal intervals (should be small) dt, and
    the point T at which we want to know the cumulative value

    This function returns the value of the integral reconstructed from the rate
    function at the point T, and it is used as a final building block to obtain
    the integral of a function.
    """
    return v0 + cumulative_change(rate_fn, 0, T, dt)

def approximate_cumulative_value_function(rate_fn, v0, dt):
    """Returns the approximate cumulative value (area under the function)
    given a rate function, an initial value v0 and a value for the length
    of the infinitesimal interval (should be small)

    This functions returns the integral of the rate function. The difference
    with `get_cumulative_value_function(...)` is that the latter takes into
    account the tolerance values in order to find the appropriate value for dt.
    """
    def cumulative_value_function(T):
        return approximate_cumulative_value(rate_fn, v0, dt, T)
    return cumulative_value_function


def get_cumulative_value_function(rate_fn, v0, digits=6):
    """Returns the approximate cumulative value (area under the function)
    given a rate function, an initial value v0 and and a tolerance for the
    approximation.

    This functions returns the integral of the rate function.
    """
    def cumulative_value_function(T):
        tolerance = 10 ** (-digits)
        dt = 1
        approx = v0 + cumulative_change(rate_fn, 0, T, dt)
        for _ in range(0, digits * 2):
            dt = dt / 10
            next_approx = v0 + cumulative_change(rate_fn, 0, T, dt)
            if abs(next_approx - approx) < tolerance:
                return round(next_approx,digits)
            else:
                approx = next_approx
        raise Exception("Integral did not converge after {} iterations!".format(digits * 2))
    return cumulative_value_function


## Now some syntactic sugar for other scenarios, using top-bottom approach
def get_integral_function(derivative_fn, int0, digits = 6):
    """Returns the approximate integral function given a function
    derivative_fn, and the initial value for the integral function int0.
    You can optionally pass the tolerance for the approximation.
    """
    return get_cumulative_value_function(derivative_fn, int0, digits)

def approximate_integral_value(derivative_fn, int0, dx, x):
    """Returns the approximate value (area under the graph)
    given a derivative function deritvative_fn, an initial value for
    the cumulative value int0, a value for the length of the infinitesimal
    intervals (should be small) dx, and the point x at which we want to know
    the value of the integral function.

    Note that you can also get that value in a more accurate way using
    `get_integral_function()`, but approximate_integral_value() is faster.
    """
    return approximate_cumulative_value(derivative_fn, int0, dx, x)

######## Derivatives
def average_rate(f, x1, x2):
    """Returns the average rate of change for the function f between the points
    x1 and x2.
    That is, this function returns the slope of the secant line between f(t1) and f(t2).
    """
    return (f(x2) - f(x1))/(x2 - x1)

def approximate_average_rate(f, x, digits = 6):
    """Returns the approximate value of the average rate (that is the derivative)
    of a given function f at the point x for a given precision specified by a
    number of digits."""
    tolerance = 10 ** (-digits)
    h = 1
    approx = average_rate(f, x - h, x + h)
    for _ in range(0, 2 * digits):
        h = h / 10
        next_approx = average_rate(f, x - h, x + h)
        if abs(next_approx - approx) < tolerance:
            return round(next_approx, digits)
        else:
            approx = next_approx
    raise Exception('Derivative did not converge in {} iterations'.format(2 * digits))


def get_approximate_average_rate_function(f, digits=6):
    """Returns the approximate function for the average rate of change of
    a function f (that is the derivative) with given precision"""
    def average_rate_function(t):
        return approximate_average_rate(f, t, digits)
    return average_rate_function

# And some syntactic sugar for derivatives
def get_approximate_derivative_function(f, digits=6):
    """Returns the approximate derivative function for the given function
    with given precision"""
    def average_rate_function(t):
        return approximate_average_rate(f, t, digits)
    return average_rate_function

def approximate_derivative_value(f, x, digits = 6):
    """Returns the approximate value of the derivative of a given function f
    at the point x for a given precision specified by a number of digits."""
    tolerance = 10 ** (-digits)
    h = 1
    approx = average_rate(f, x - h, x + h)
    for _ in range(0, 2 * digits):
        h = h / 10
        next_approx = average_rate(f, x - h, x + h)
        if abs(next_approx - approx) < tolerance:
            return round(next_approx, digits)
        else:
            approx = next_approx
    raise Exception('Derivative did not converge in {} iterations'.format(2 * digits))
