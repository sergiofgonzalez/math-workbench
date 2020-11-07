import numpy as np
import matplotlib.pyplot as plt 

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