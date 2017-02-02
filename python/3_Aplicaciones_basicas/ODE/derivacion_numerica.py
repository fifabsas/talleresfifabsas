# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 20:03:38 2015
 
@author: FIFA
 
Derivación numérica
"""
 
import numpy as np
from matplotlib import pyplot as plt
 
def dy_foward(y,h):
    #Derivación numérica. Y es la imagen y h el paso de división. Debe coincidir con el paso de x.
    N = len(y)
    dy = np.zeros(N)
    for k in range(N-1):
        dy[k]=(y[k+1]-y[k])/h
    return dy
     
def ddy_foward(y,h):
    #Segunda derivada. Y es la imagen y h el paso de la división. Debe coincidir con el paso de x.
    N = len(y)
    ddy = np.zeros(N)
    for k in range(1,N-1):
        ddy[k]= (y[k+1]-2*y[k] + y[k-1])/(h**2)
    return ddy
     
     
x = np.arange(0, np.pi*2, 0.01)
y = np.sin(x)
dy = dy_foward(y, 0.01)
ddy = ddy_foward(y,0.01)
plt.scatter(x, y)
plt.scatter(x, dy, color='r')
plt.scatter(x,ddy, color='g')
plt.show()
