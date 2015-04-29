import matplotlib.pyplot as plt
import numpy as np

# Vectores que voy a graficar
x = np.arange(10)
y = x**2

# El comando subplot devuelve dos objetos: la ventana (fig) y los contenidos (sub)
fig,sub = plt.subplots(2)

# Configuro las propiedades de cada sub-grafico
sub[0].plot(x, y)
sub[0].set_ylabel('Ordenadas 1')
sub[0].set_title('Título 1')
sub[0].grid(True)

sub[1].plot(x, np.sqrt(y))
sub[1].set_xlabel('Valores de x')
sub[1].set_ylabel('Ordenadas 1')
sub[1].grid(True)

# draw() es necesario para que se efectúen los cambios
plt.draw()
# show() muestra los gráficos. Conviene que esto suceda una sola vez así no tiene que dibujar cada vez que cambio alguna propiedad
plt.show()
