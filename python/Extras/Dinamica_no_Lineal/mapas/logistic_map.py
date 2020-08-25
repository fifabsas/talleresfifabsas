# -*- coding: UTF-8 -*-

from matplotlib import pyplot as plt
import numpy as np

################################################################################

def logistic(x, r):
    """Logistic map, with parameter r."""
    return r * x * (1 - x)

def bif_plot(x0, rs, axes):
    """Bifurcation plot for the logistic map.
    Inputs: x0 - initial condition.
            rs - Numpy array with values for
                 parameter r.
            axes - matplotib axes object."""
    y = np.zeros([2, 50])
    for r in rs:
        x = np.arange(x0, 800)
        for i in xrange(len(x)-1):
            x[i+1] = logistic(x[i], r)

        y[0, :] = r
        y[1, :] = x[-50:]
        axes.plot(y[0, :], y[1, :], 'b.')

################################################################################

if __name__=='__main__':
    # parameter definitions
    rs = np.linspace(0.001, 4, 2000) # values for the parameter r
    x0 = .5 #initial condition for x

    fig = plt.figure()
    ax = fig.add_subplot(111)
    bif_plot(x0, rs, ax)
    plt.show(fig)
