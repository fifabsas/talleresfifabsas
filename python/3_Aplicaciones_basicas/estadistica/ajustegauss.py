from scipy.stats import norm
from numpy import linspace
import matplotlib.pyplot as plt

#armo una lista de 150 numeros distribuidos al azar
#con distribucion gaussiana de media 0 y des str igual a 1
dist_normal = norm.rvs(loc=0,scale=1)   #rvs = Random variates.

# ajusto mi distribucion
parametros = norm.fit(dist_normal) 

#esta funcion me devuelve dos datos: 
#la media y la des str en una lista

print parametros  # similar a (0,1)

x = linspace(-5,5,100)
# print x


#distribucion que ajuste
pdf_fitted = norm.pdf(x,loc = parametros [0],scale = parametros [1])   # pdf = Probability density function.
# distribucion original
pdf = norm.pdf(x)

# en el grafico en azul esta la distribucion original
# y en rojo, la que ajuste.
plt.plot(x,pdf_fitted,'r-',x,pdf,'b-')
