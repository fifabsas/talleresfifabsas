# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 16:50:29 2015

@author: FIFA

Aplicación del ajuste lineal sobre un conjunto sintetico de datos para ilustrar el ajuste de cuadrados minimos

"""

import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2.1, 2.9, 3.5, 4.1, 6.2, 7.4, 7.9, 9.2, 10.1])
y = np.array([1.26, 4.75, 8.91, 7.93, 10.34, 16.7, 18.04, 20.87, 23.37, 27.02])


#plt.plot(x, y, 'ob')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()

N = len(x)

num_a = N * np.sum(x*y) - np.sum(x) * np.sum(y)
delta = N * np.sum(x**2) - np.sum(x)**2
a = num_a/delta

num_b = np.sum(x**2) * np.sum(y) - np.sum(x) * np.sum(x*y)
b = num_b/delta

sigmay = np.sqrt( (1/(N-2)) * np.sum( (y - (a*x+b))**2 ) )
sigmaa = sigmay * np.sqrt( N/delta )
sigmab = sigmay * np.sqrt( np.sum(x**2)/delta )

R2 = (num_a)**2 / ( (N*np.sum(x**2)-np.sum(x)**2) * (N*np.sum(y**2)-np.sum(y)**2) )

plt.plot(x, y, 'ob', x, a*x+b, '-r')
plt.xlabel('x [unidades de x]')
plt.ylabel('y [unidades de y]')
plt.title('Ajuste de cuadrados minimos')
plt.legend(("Datos","Ajuste"), loc=4)
plt.text(1, 25, 'R$^2$ = 0.989', fontsize=14)
plt.grid('on')

plt.show()
