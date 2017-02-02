
# coding: utf-8

# #Taller introductorio de Python
# ![taller_python](https://raw.githubusercontent.com/fifabsas/talleresfifabsas/master/python/introductorio/fig/Python.png)
# ##Temario
# 
# * Entrada y salida de datos por consola
# * Variables y operaciones:
#     - Enteros (intergers)
#     - Punto flotante (floats)
#     - Booleanos
#     - Listas (y tal vez tuplas)
# * Condicionales y ciclos: if, for and while
# * Funciones def y lambda
# * Gráficos:
#     - Creación de una lista de valores aleatorios
#     - Gráfico en scatter y plot

# ##Entrada y salida de datos
# Todo programa necesita recibir una entrada de datos y sacar una salida de datos, por más rudimentaria o fija que sea. Lo más rápido es usar la consola de texto, con _print_ y _input_

# In[4]:

#Los comentarios son líneas, o partes de una línea, que no se leen, y ayudan a entender el código.
#Empiezan con # todas

#Acá imprimos en pantalla
print("Hola mundo")
print(5 + 5)


# In[3]:

text = input("Ingresá algo: ")
print("Ingresaste " + text)


# ## Variables
# Las variables son pedazos de la memoria de la computadora que pueden variar con el avance del programa. Para mejorar la legibilidad y la usabilidad del código, existen los **tipos** de datos

# In[8]:

integer = 5  #Números "enteros"
print(type(integer))
flotante = 5.0 #Números "reales"
print(type(flotante))

division = integer / flotante #Divisón no entera por defecto en Python v3.x
print(division)

division = int(division)   #Transformación a entero
print(division,'\t', type(division))

# En la próxima entrega vamos a ver otras funcionalidades con Numpy

# Los tipos booleanos o de verdad son muy útiles para escribir relaciones lógicas
boolean = 5==4
# <, >, >=, <=, != son comparadores booleanos
# and, or, not son conjuntores para hacer frases lógicas más complicadas.
# Para lo demás, hay que usar las leyes de DeMorgan.
print(boolean, '\t', type(boolean))

# Las listas pueden mantener varias variables con diferentes tipos y valores. Son como una bolsa ordenada de datos.
lista1 = [1, 2, 3]
print(lista1)
print(lista1[1])
print(lista1[-1])

lista2 = [4, 5, 6]
lista3 = ['a', 'b', boolean, integer, 'Todo Python ahi adentro']

#Agrego al final a una lista
lista1.append(3)
print(lista1)

#Agrego una lista a otra lista
lista1.append(lista2)
print(lista1)

#"Sumo" las listas
lista1.extend(lista2)
print(lista1)

print(lista3.pop()) #Devuelve el último elemento
print(lista3) #Y no está más en la lista

# Probar los métodos insert, remove, pop, sort de las listas


# ##Condicionales y ciclos
# ***Repetir y controlar***; si necesitamos repetir cosas, no escribir mil veces el mismo código, usar un ciclo (for, while). Y si es necesario decidir sobre dos cosas, condicionales (ifs)

# In[14]:

boolean = True #Cambiar para ver resultados

# Control de flujo de código con condicionales (Ifs).
if boolean == True:
    boolean = True

# Se puede volver tan complejo como uno quiera
if 5>4:
    if 3 >2:
        if 2>1:
            if 1>0:
                print('Cadena de ifs')

# También podemos agregarle un "si no"
if boolean == True:
    boolean = False
else:
    boolean = True
    
# Y también, un "si no, si"
if boolean == True:
    print("True")
elif 1 < 5:  #Cambiar para ver resultados
    print(False)
else:
    print("Finalmente")


# ### Bucles
# Con esto, vamos a poder imprimir muchos hola mundo

# In[28]:

nueva_lista = []
# Bucles con tamaño fijo
for i in range(20):
    nueva_lista.append(i)
print(nueva_lista)

if len(nueva_lista) <= 20:
    for i in range(20):
        nueva_lista.append(i)
print(nueva_lista)

#Bucles de tamaño no necesariamente fijo
#OJO que pueden ser infinitos y nunca terminar. Para eso Ctrl+C y detiene la operación
i = 0
while i < 20:
    print(i - 1)
    i += 1


# ##Funciones
# A veces hay que repetir código en muchos lugares, para lo que no hay que repetir con Ctrl+C y Ctrl+V, use *funciones*

# In[21]:

def suma(a, b):
    c = a + b
    return c #Devuelvo el resultado

print(suma(2, 3))

def factorial(n):
    j = 1
    for i in range(1, n + 1): #EL range va de 0 a n, no inclusive
        j *= i 
    return j

print(factorial(5))


# In[27]:

#Funciones anónimas o lambdas, una forma rápida de hacer una función simple
par = lambda n: n%2 == 0 #Me devuelve True si es par
print(type(par), '\t', par(5))  #Las funciones tienen tipo!!!


# ## Gráficos
# Acá hacemos un acercamiento básico a los gráficos, para perderle el miedo nomás. En la próxima entrega vamos a trabajar de forma más exhautiva con los gráficos y datos

# In[30]:

#Importo los paquetes para ser usados después
import numpy as np
from matplotlib import pyplot as plt
get_ipython().magic('matplotlib inline')


# In[32]:

import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(-5, 5) #Por defecto son 50 números equispaciados entre -5 y 5

#Ahora creamos la variable dependiente, con algun de ruido para "crear datos"
y = x**2 -3
ruido = np.random.rand(len(y))*0.8
y = y+ruido

#Con esto graficamos una variable contra otra
plt.plot(x, y, 'bo')
plt.xlabel('Variable independiente')
plt.ylabel('x^2')
plt.grid()

plt.show() #Si corrés en Ipython con %matplotlib inline no es necesario


# In[ ]:



