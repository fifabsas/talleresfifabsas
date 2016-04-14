# -*- coding: utf-8 -*-
"""
Ajuste lineal
"""
def ajustelineal(x,y,errores):
    """
    Ajusta los datos con una recta lineal en el sentido de max verosimilitud
    errores es un array con las desviaciones estándar de los valores y
    x es un array con los valores independientes (sin error)
    y es un array con los datos medidos que se desea ajustar
    ---
    Devuelve: slope,intercept,r2,chi2,pcov
    pcov es la matriz de covarianza de slope e intercept
	slope = slope +- sqrt(pcov[0,0])
	intercept = intercept +- sqrt(pcov[1,1])
    """
    import numpy as np
    # Supongo mediciones no correlacionadas --> V prop. Id.
    # El ajuste es lineal en x, pero puede ser lineal en theta
    N = len(x)
    A = np.ones((N,2))
    A[:,1] = x
    Vi = np.diag(1/errores**2)
    
    pcov = np.linalg.inv( np.dot(np.transpose(A),np.dot(Vi,A)))
    theta = np.dot(np.dot(pcov, np.transpose(A)),np.dot(Vi,y))
    slope = theta[1]
    intercept = theta[0]
    
    # Coeficiente R2
    fit = theta[0]+theta[1]*x
    r2 = 1 - sum((y-fit)**2)/sum((y-np.mean(y))**2)
    # Coeficiente Chi2
    chi2 = np.dot(np.transpose(y-fit),np.dot(Vi,y-fit))/(N-2)
    return slope,intercept,r2,chi2,pcov
"""
plt.figure(1)
plt.clf()
plt.grid()
plt.errorbar(x,y,fmt='o',yerr=errores)

z = np.linspace(x[0],x[-1],1000)
plt.plot(z,theta[0]+theta[1]*z,'r')
print("R^2 =",r2)
print("Chi^2 =",chi2)
"""
