# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 20:03:38 2015
 
@author: FIFA
 
Derivación numérica
Los datos están en esta misma carpeta en los archivos Integraciondata%d.txt
"""
 
import numpy as np
from matplotlib import pyplot as plt
 
def leertab(filename, skiplines=0): #Defino la funcion para importar los Datos (Esta en Importacion de Datos)
    import numpy as np
    return np.loadtxt(filename, delimiter='\t', skiprows=skiplines,
                      usecols=(),  unpack=True)
                      
def integrar(y, x): #Defino una función que integre por trapecios
    Area = np.zeros(len(x))
    for i in np.arange(1,len(x)):
        Area[i] = Area[i-1] + x[i]*y[i]
    return Area
    
Datos = leertab('Integraciondata1.txt', 4); #¿Te animás a crear el loop para analizar más datos?

tiempo = Datos[1,:]
H = Datos[2,:]
dI = Datos[3,:]

Bpropia = integrar(dI, tiempo) #¿y si quisiesemos integrar por alguna otra regla?

Bnp = np.cumsum(dI*tiempo)


plt.scatter(H, Bpropia)
plt.scatter(H, Bnp, color='r')
plt.show()
