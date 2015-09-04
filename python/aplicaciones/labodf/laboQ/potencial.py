# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""


import numpy as np
import matplotlib.pyplot as plt

#Acá deberías traer la matriz
#A = np.loadtxt("data")
Nx = 5
Ny = 5
A = np.random.rand(Nx + 1, Ny + 1)
print(np.shape(A))
A[:,0] = np.array([0] + list(range(Nx)))
A[0,:] = np.array([0] + list(range(Ny)))
print(A)

plt.figure(1)
plt.imshow(A[1:,1:]) #Genera una imagen
plt.figure(2)
plt.contour(A[1:,0], A[1,1:], A[1:,1:], np.linspace(0, 2, 100)) #Genera el contorno
plt.show()