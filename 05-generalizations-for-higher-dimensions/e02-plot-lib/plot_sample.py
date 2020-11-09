from my_plot import plot
from math import sin

def f(x):
    return 0.5 * x + 3

def g(x):
    return sin(x)

def add_functions(f, g):
    def new_function(x):
        return f(x) + g(x)
    return new_function

plot([f, g, add_functions(f, g)], -10, 10, 'Visualizing function addition')