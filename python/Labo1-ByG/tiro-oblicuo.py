import numpy as np
import matplotlib.pyplot as plt
"""
Este es un script para visualizar:
1) Alcance de un proyectil lanzado con velocidad inicial v0 vs. ángulo de disparo.
2) Distintas trayectorias del proyectil.
"""
# Algunas constantes y variables
g = 9.8
v0 = 25

# Alcance como función del ángulo inicial de disparo (fórmula calculada a mano)
def alcance(th,v0):
    return v0**2/g*np.sin(2*th)
theta = np.linspace(0,np.pi/2,500)
plt.figure(1)
plt.plot(theta/2/np.pi*360,alcance(theta,v0))
plt.xlabel("Ángulo inicial de disparo [°]")
plt.ylabel("Alcance [m]")
plt.grid()

# Trayectoria (fórmula calculada a mano)
def tray(x,th,v0):
    return np.tan(th)*x-g*x**2/(2*v0**2*np.cos(th)**2)

plt.figure(2)
for angulo in np.linspace(0,np.pi/2,9)[1:-1]:
    x = np.linspace(0,v0**2/g*np.sin(2*angulo),500)
    plt.plot(x,tray(x,angulo,v0),'-',label="$\Theta$ = "+str(int(angulo/2/np.pi*360))+"°")
plt.legend(loc=0)
plt.xlabel("Distancia [m]")
plt.ylabel("Altitud [m]")
plt.grid()
plt.title("Tiro oblicuo para distintos ángulos")

plt.show()
