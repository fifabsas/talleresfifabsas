# -*- coding: utf-8 -*-
#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import scipy.misc
import os
import scipy.optimize as opt
import scipy.stats as stats
from instrumental import Osciloscopio


#Ingresa el path para guardar los datos

def adquirirDatos(path):
    os.chdir(path)
    #Ingresa tipo de distribución al comparar. Pueden ser ambas

    #Parámetros de los experimentos
    escalaT = 100E-6 #Tiempo de medición. Tiempo en qué integra el osciloscopio. Considerar coherencia
    escalaV = 10E-3 #Escala de tensión. 
    #thres = -5e-3 #Tensiones mayores a este valor (del PMT se observa tensiones negativas) es **ruido**
    N = 10 #Número de experimentos

    osci = Osciloscopio('USB0::0x0699::0x0363::C065087::INSTR')
    open("eventos.csv","w").close()
    open("cuentas.csv","w").close()
    #cuentas = []
    for i in range(N):
        #eventos = []
        osci.setTiempo(escala = escalaT, cero = 0) #No afecta la medición cambiar el cero del tiempo
        osci.setCanal(canal = 1, escala = escalaV, cero = 0)		
    #print(osci.getCanal(canal = 1))    
        tiempo, data = osci.getVentana(1); #Mide en el canal 1
    
        np.savetxt("medicion_{0}.csv".format(i), 
                   np.vstack((tiempo,data)).T, delimiter=',') #Guarda los datos crudos, separados por ,
    

        #minimos = (np.diff(np.sign(np.diff(data))) > 0).nonzero()[0] + 1  #Mínimos
        #Elimino tensiones positivas, recodar que la señal del PMT es negativa
        #for m in minimos:
        #    if data[m] < thres:
        #        eventos.append(data[m])
        #cuentas.append(len(eventos))            
    #np.savetxt("eventos.csv",eventos, delimiter=',')
    #np.savetxt("cuentas.csv",cuentas, delimiter=',')
    
def generarCuentas(medicionesPath, nMed = 1000, thres = -5e-3):
    os.chdir(medicionesPath)
    mediciones = []
    for i in os.listdir("."):
        if i.find('med') != -1:
            mediciones.append(i)
        if len(mediciones) == nMed:
            break
    #Listar mediciones
    cuentas = []
    for med in mediciones:
        data = np.loadtxt(med, delimiter=',')
        minimos = (np.diff(np.sign(np.diff(data[:,1]))) > 0).nonzero()[0] + 1  #Mínimos
        cuentas.append(data[data[minimos,1] < thres].shape[0])
    #plt.show()
    #print(cuentas)            
    #np.savetxt("eventos.csv",eventos, delimiter=',')
    #Crear carpeta ./histograma/ y guardar
    try:
        os.mkdir('./histograma') #Accedo si existe
    except:
        pass
    os.chdir('./histograma')
    
    np.savetxt("cuentas.csv",cuentas, fmt='%i', delimiter=',')
    

def correlacion(dataPath):
    data = np.loadtxt(dataPath, delimiter=',')
    data = data[:]

    autocorre = np.correlate(data[:,1],data[:,1],mode="same")
    
    plt.plot(data[:,0],data[:,1])
    plt.figure()
    plt.plot(autocorre)
    plt.xlabel("t[s]")
    plt.ylabel('Amp[V]')
    plt.show()
    
def histograma(path):
    
    ### Datos ###
    os.chdir(path)      
    rawData = np.loadtxt('cuentas.csv', delimiter=',') #carga cuentas.csv. Guardar con savetxt
    data = rawData[rawData < 20] #Acá podés eliminar cuentas muy altas, producto de malas mediciones
    data.sort()
    ###
    ### Histograma ###
    hist, bins = np.histogram(data,bins = np.arange(np.max(data)), density = True)
    bins = bins[:-1]
    ###
    ### Ajuste ###
    ### Fuciones de ayuda ###
    poissonPDF = lambda j, lambd: (lambd**j) * np.exp(-lambd) / scipy.misc.factorial(j)
    bePDF = lambda j, lambd: np.power(lambd, j) / np.power(1+lambd,1+j)
    ###
    pPoisson, pconv = opt.curve_fit(poissonPDF, bins, hist, p0 = 3)
    pBE, pconv = opt.curve_fit(bePDF, bins, hist, p0 = 3)
    with open('p-valor','w+') as f:
        f.write("Poisson p-value: {}\n".format(stats.chisquare(hist,poissonPDF(bins,pPoisson),ddof = 1)[1]))
        f.write("BE p-value: {}".format(stats.chisquare(hist,bePDF(bins,pBE),ddof = 1)[1]))
    ######
    
    ### Ploteo ###
    width = 24 / 2.54 #24cm de ancho
    figSize = (width * (1+np.sqrt(5)) / 2, width) #relación aurea
    
    #Figura 1    
    plt.figure(figsize=figSize)
    plt.plot(poissonPDF(bins,pPoisson), 'r^', label='Poisson', markersize = 10) #azul
    plt.plot(bePDF(bins,pBE), 'go', label = 'BE', markersize = 10) #verde
    plt.bar(bins,hist, width = 0.1,label='Datos')    
    #Configuración
    plt.grid()
    ### Ejes ###
    plt.axis('tight')
    plt.xlim((-1,10))
    plt.ylim((0,0.25))
    plt.xlabel('Numero de eventos',fontsize=22)
    plt.ylabel('Frecuencias relativas',fontsize=22)
    plt.tick_params(labelsize = 20)
    ###
    ### Texto a agregar ###
    text = 'Poisson\n'
    text += r'$<n> = {0:.2f}$'.format(pPoisson[0])
    text += '\n'
    text += r'$\chi^2_{{ \nu = {0} }} = {1:.3f}$'.format(hist.size, poissonChisq)
    text += '\n\n'
    text += 'BE\n'
    text += r'$<n> = {0:.2f}$'.format(pBE[0])
    text += '\n'
    text += r'$\chi^2_{{ \nu = {0} }} = {1:.2f}$'.format(hist.size, beChisq)
    plt.text(0.7,0.3, text, transform = plt.gca().transAxes, fontsize = fontSize)
    ######
    plt.legend(loc=0,fontsize=20)
    plt.savefig('histograma.png', bbox_inches = 'tight')
    
    #Figura 2
    plt.figure(2,figsize=figSize)
    plt.plot(np.log(poissonPDF(bins,pPoisson)), 'r^', label='Log(Poisson)', markersize = 10) #azul
    plt.plot(np.log(bePDF(bins,pBE)), 'go', label = 'Log(BE)', markersize = 10) #verde
    plt.plot(bins,np.log(hist),'bd',label='Log(Datos)', markersize = 10)    
    #### Configuración ####
    plt.grid()
    ### Ejes ###
    plt.axis('tight')
    plt.xlim((-1,10))
    plt.ylim((-5,-1))
    plt.xlabel('Numero de eventos',fontsize=22)
    plt.ylabel('Log(Frecuencias relativas)',fontsize=22)
    plt.tick_params(labelsize = 20)
    ###
    plt.legend(loc=0,fontsize=20)
    ########
    plt.savefig('log_histograma.png', bbox_inches = 'tight')
