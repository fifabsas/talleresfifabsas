import numpy as np
import matplotlib.pyplot as plt
"""
Este es un script para visualizar la trayectoria de un proyectil
"""
# Defino las constantes del problema
g = 9.8
v0 = 25
angulo = np.pi/4

# Creo la función que define la trayectoria y(x) (fórmula calculada a mano)
def tray(x,th,v0):
    return np.tan(th)*x-g*x**2/(2*v0**2*np.cos(th)**2)

# Abro una nueva figura
plt.figure()
# Defino el dominio que tiene 500 puntos entre 0 y 63.76 (¿por qué usamos este número? ¡Prueben otros!)
x = np.linspace(0,63.76,500)
# Defino la imagen
y = tray(x,angulo,v0)
# Grafico tray(x) con la velocidad inicial y ángulo antes definidos
plt.plot(x,y)

### De ahora en más decoramos un poco la ventana
# Agrego un poco de descripción a la ventana
plt.title("Tiro oblicuo")
plt.xlabel("Distancia [m]")
plt.ylabel("Altitud [m]")
# Agrego la grilla
plt.grid()

# Muestro la ventana de gráfico
plt.show()
