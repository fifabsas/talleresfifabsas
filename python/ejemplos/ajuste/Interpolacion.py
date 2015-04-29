# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 16:55:01 2015

@author: FIFA

Ver documentation en:http://docs.scipy.org/doc/scipy-0.15.1/reference/generated/scipy.interpolate.interp1d.html
                     http://docs.scipy.org/doc/scipy-0.15.1/reference/generated/scipy.interpolate.lagrange.html#scipy.interpolate.lagrange

"""

from scipy.interpolate import interp1d, lagrange

import matplotlib.pyplot as plt
import numpy as np


#------------ejemplo----------

x = np.linspace(0, 10, 10)
y = np.cos(-x**2/8.0)
f = interp1d(x, y)
f2 = interp1d(x, y, kind='cubic')
f3 = lagrange(x, y)


xnew = np.linspace(0, 10, 40)


plt.plot(x,y,'o',xnew,f(xnew),'-', xnew, f2(xnew),'--', xnew, f3(xnew), '.')
plt.legend(['data', 'linear', 'cubic', 'Lagrange'], loc='best')
plt.xlabel('x')
plt.ylabel('y')
print f3, type(f3)




plt.show()
