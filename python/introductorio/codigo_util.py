print('Hola mundo')
print('\t')
print('Mi nuevo mundo')

texto = raw_input('Escribi algo: ')

print('Acabas de decir: ' + '"' + texto + '"')




#Variables
#--------------------------------------------------------------------------------------

integer = 5

print type(integer)

flotante = 5.0

print type(flotante)

division = integer / flotante
# +, -, *, **, log(), exp, pow. >>>>> Numpy!

print division

division = int(division)

print division,'\t', type(division)

#round, ceil, floor, trunc >>>>>> Numpy!


boolean = 5==4
# <, >, >=, <=, !=

print boolean, '\t', type(boolean)


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

#probar insert, remove, pop, sort
#que cosas se pueden hacer con tuplas?


#Funciones, condicionales y ciclos
#------------------------------------------------------------------------------

if boolean == True:
    boolean = False
    
if 5>4:
    if 3 >2:
        if 2>1:
            if 1>0:
                print 'Cadena de ifs'


nueva_lista = []
for i in range (20):
    nueva_lista.append(i)
    
print nueva_lista

if len(nueva_lista) <= 20:
    for i in range(20):
        nueva_lista.append(i)
        
print nueva_lista

def factorialcasero(n):
    resultado = 1
    for i in range(n):
        resultado *= i+1
    return resultado

print factorialcasero(6)

par = lambda n: n%2 == 0 #Me devuelve True si es par

print type(par), '\t', par(5)



#Gráficos
#---------------------------------------------------------------------------------

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
