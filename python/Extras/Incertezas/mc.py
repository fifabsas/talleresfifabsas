import numpy as np
import scipy as sp
from scipy import optimize
import matplotlib.pyplot as plt

data = np.loadtxt("doble_exp.dat")
x = data[:,0]
y = data[:,1]
error_y = data[:,2]

f = lambda x, A, B, C, D, E: A + B * np.exp(C*x) + D * np.exp(E*x)

p0 = (10, 130, -0.001, 960, -0.02)

#MMCC
M = []
j = 0
N = 10000
for i in range(N):
    #Vuelvo a computar y
    yp = y + np.random.randn(y.shape[0]) * error_y
    
    p0 = (10, 10, -0.001, max(y), -0.02)
    
    try:
        p, _ = sp.optimize.curve_fit(f, x, yp, p0=p0)
        M.append(p)
    except RuntimeError:
        j += 1
print("Tasa de error de ajuste: {}".format(j/N))
M = np.array(M)

#Valor medio y covarianza
p = np.mean(M, axis=0)
cov = np.cov(M.T)

print(p, cov)

t = np.linspace(min(x), max(x), 1000)
plt.plot(t, f(t, *p), 'r-', x, y, 'bo')
plt.yscale('log')
plt.show()
