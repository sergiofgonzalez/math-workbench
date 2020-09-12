#
# Matplotlib: the best invention after the sliced bread
#

import matplotlib.pyplot as plt   # pyplot is the plotting module from Matplotlib, typically aliased to plt

#
## Scatter plot: useful for visualizing collections of ordered pairs in the form (x, y)
#
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]
plt.scatter(x_values, y_values)
plt.show()  # this statement is blocking

# You can use marker and c arguments to set the shape and color of the dots
plt.scatter(x_values, y_values, marker='x', c='red')
plt.show()


#
## Line chart: points are connected with lines
#
plt.plot(x_values, y_values)
plt.show()

# line charts are also useful to draw segments
def plot_segment(p1, p2):
  x1, y1 = p1
  x2, y2 = p2
  plt.plot([x1, x2], [y1, y2], marker='o')
  plt.show()

plot_segment((0,3), (2, 1))

# line charts are also useful to draw the graph of a function: given a function f, plotting all the pairs (x, f(x)) in some range
import numpy as np
x_values = np.arange(0, 10, 0.01)
y_values = np.sin(x_values)
plt.plot(x_values, y_values)
y_values = np.cos(x_values)
plt.plot(x_values, y_values, c="red")
plt.show()


#
## Some common customizations (more on matplotlib.org)
#

# Setting the scale (by default is autoscaled by matplotlib)
plt.xlim(0, 5)    # set x range to be (0, 5)
plt.ylim(0, 5)    # set y range to be (0, 5)
plot_segment((0,3), (2, 1))

# making x units and y units equal (so that the graph is square)
plt.xlim(0, 5)    # set x range to be (0, 5)
plt.ylim(0, 5)    # set y range to be (0, 5)
plt.gcf().set_size_inches(5, 5)  # gcf stands for get current figure
plot_segment((0,3), (2, 1))

# setting labels
x_values = np.arange(0, 10, 0.01)
y_values = np.sin(x_values)
plt.plot(x_values, y_values)
plt.title('Graph of sin(x) vs. x', fontsize=16)
plt.xlabel('this is the x value', fontsize=16)
plt.ylabel('this is the y label', fontsize=16)
plt.show()