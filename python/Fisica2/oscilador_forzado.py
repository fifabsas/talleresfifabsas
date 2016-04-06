# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 12:18:55 2016

@author: Nicolás Torasso - nicolas.torasso@gmail.com

Este es un código para visualizar la solución completa del oscilador
armónico forzado con amortiguamiento. Se compara con la solución analítica.
"""
# Importo los módulos a usar de las bibliotecas
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

plt.clf()#Limpia todas las ventanas de gráfico abiertas
plt.figure(1)# Abro la ventana de gráfico que voy a usar

# Defino los parámetros del forzante y la función
F = 1
w = 10
delta = 0
def forzante(t):
    return F*np.cos(w*t+delta)
    
# Defino los parámetros del oscilador: amortiguación y frecuencia propia
gamma = 1
w0 = 5
def ecdif(X,t):
    return np.array([X[1] , -gamma*X[1]-w0**2*X[0]+forzante(t)])

# Defino el vector con las condiciones iniciales (x0 y v0)
# Defino el vector de tiempos para los cuales obtengo la sc numérica
X0 = np.array([2,0])
t = np.linspace(0,50,1000)
solucion = odeint(ecdif,X0,t)

# Grafico
plt.plot(t,solucion[:,0],label='Sc. numérica')
plt.plot(t,forzante(t),'r.-',label='Forzante')

# Defino la sc analítica completa
def sc_analitica(t):
    wg = np.sqrt( w0**2-(gamma/2)**2 )
    A = F/np.sqrt( (gamma*w)**2 + (w0**2-w**2)**2 )
    theta = delta-np.arctan(gamma*w/(w0**2-w**2))
    
    c1 = X0[0] - A*np.cos(theta)
    c2 = (X0[1]+gamma*X0[0]/2-gamma*np.cos(theta)/2+A*w*np.sin(theta))/wg

    xh = np.exp(-gamma*t/2)*(c1*np.cos(wg*t) + c2*np.sin(wg*t))    
    xp = A*np.cos(w*t+theta)
    return xh + xp
plt.plot(t,sc_analitica(t),'k*-',label='Sc. analítica')

# Agrego nombres al gráficoy a los ejes
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.title('Oscilador forzado')
plt.legend(loc=0)