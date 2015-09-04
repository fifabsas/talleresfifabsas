# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt


A = np.loadtxt("matriz.dat")

plt.figure(1)
plt.contourf(A[0,1:],A[1:,0],A[1:,1:]) #Genera el contorno

plt.show()
