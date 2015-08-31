# -*- coding: utf-8 -*-

# #Curso introductorio de Python

# ##Lista de temas: 


# * Print y raw_input

# * Variables y operaciones:

#    - Integers
#    - Floats
#    - Booleans
#    - List and tuples

# * Condicionales y ciclos: if, for and while

# * Funciones def y lambda

# * Gráficos:
#   - Creación de una lista de valores aleatorios
#   - Gráfico en scatter y plot



print('Hola mundo')
print('\t')
print('Mi nuevo mundo')


# #Entrada y salida, como interaccionar con Python
#texto = raw_input('Escribi algo: ')
#print('Acabas de decir: ' + '"' + texto + '"')


# #Variables
# Acá vamos a crear algunas variables con sus respetivos tipos

integer = 5
print type(integer)
flotante = 5.0
print type(flotante)

division = integer / flotante
print division

division = int(division)   #Transformación a entero
print division,'\t', type(division)

# En la próxima entrega vamos a ver otras funcionalidades con Numpy
# Los tipos booleanos o de verdad son muy útiles para escribir relaciones lógicas
boolean = 5==4
# <, >, >=, <=, !=
print boolean, '\t', type(boolean)

# Las listas pueden mantener varias variables con diferentes tipos y valores. Son como una bolsa ordenada de datos.
lista1= [1, 2, 3]
print lista1[1]

lista2= [4, 5, 6]
lista3= ['a', 'b', boolean, integer, 'Todo Python ahi adentro']

lista1.append(3)
print lista1

lista1.append(lista2)
print lista1
lista1.extend(lista2)
print lista1

# Probar los métodos insert, remove, pop, sort de las listas


# ##Funciones, condicionales y ciclos

# Control de flujo de código con condicionales (Ifs).
if boolean == True:
    boolean = False

# Se puede volver tan complejo como uno quiera
if 5>4:
    if 3 >2:
        if 2>1:
            if 1>0:
                print 'Cadena de ifs'

# También podemos agregarle un "si no"
if boolean == True:
    boolean = False
else:
    boolean = True
    
# Y también, un "si no, si"
if boolean == True:
    print("True")
elif 1 < 5:
    print(False)
else:
    print("Finalmente")

# ### Bucles y repeticiones
# Acá vamos a hacer algunas repeticiones
nueva_lista = []
for i in range (20):
    nueva_lista.append(i)
print(nueva_lista)

if len(nueva_lista) <= 20:
    for i in range(20):
        nueva_lista.append(i)
        
print(nueva_lista)

# ###Funciones
def factorialcasero(n):
    resultado = 1
    for i in range(n):
        resultado *= i+1
    return resultado

print(factorialcasero(6))

#Funciones anonimas o lambda
par = lambda n: n%2 == 0 #Me devuelve True si es par
print(type(par), '\t', par(5))



# ##Gráficos
import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(-5, 5)
y = x**2 -3

ruido = np.random.rand(len(y))*0.8
y = y+ruido


plt.scatter(x, y)
plt.xlabel('Variable independiente')
plt.ylabel('x^2')
plt.grid()

plt.show()
