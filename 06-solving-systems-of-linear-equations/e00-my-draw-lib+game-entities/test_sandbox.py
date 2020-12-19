import numpy as np
import matplotlib.pyplot as plt
from my_colors import black

plt3d = plt.figure().gca(projection='3d')
ax = plt.gca()

x_values = np.arange(-5, 5, 0.5)
y_values = np.arange(-5, 5, 0.5)

xx, yy = np.meshgrid(x_values, y_values)


# plane z = 2
zz = 2 * np.ones((len(xx),len(xx)), dtype=int)
plt3d.plot_surface(xx, yy, zz, alpha=0.7)

# plane x = 0
yy, zz = np.meshgrid(x_values, y_values)
xx = np.zeros((len(xx),len(xx)), dtype=int)
plt3d.plot_surface(xx, yy, zz, alpha=0.7)

# intersection between plane z=2 and x=0 is points (0, y, 2)
yy = np.linspace(-5, 5, 100)
xx = np.zeros(len(yy))
zz = 2 * np.ones(len(yy))
ax.scatter(xx, yy, zz, color=black)

ax = plt.gca()

plt.show()