import numpy as np
import matplotlib.pyplot as plt

x = [3,6,6,7,8,6,8]

# otra lista

#mu la media, sigma la desviacion standar
#el numero en np.random.randn es la cantidad de numeros

# mu, sigma = 100, 15
# x = mu + sigma * np.random.randn(10000)

bins, edges = np.histogram(x, 50)
left,right = edges[:-1],edges[1:]

X = np.array([left,right]).T.flatten()
Y = np.array([bins,bins]).T.flatten()

#hago el grafico
plt.plot(X,Y)

#pido que me muestre 
