# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 21:19:59 2015

@author: sadeus
"""

# -*- coding: utf-8 -*-
"""
Clase de manejo del perfilador
Proyecto SOMA

@author: S. Schiavinato
"""
import io
import time
import serial
import numpy as np
import pandas as pd
from serial.tools import list_ports
#import scipy as sp
#import scipy.optimize


def inputPort():
    '''Obtiene la lista de puertos, la presenta en pantalla y da 
    a elegir un puerto, devolviendo el string para conectarse
    '''
    ports = list(list_ports.comports())
    for i,p in enumerate(ports):
        print("[{}]: Puerto {}".format(i + 1, p[1]))
    port = ""
    if len(ports) > 0:
        port = ports[int(input("Ingrese el puerto serie: ")) - 1][0]
    return port
    
def update(serialObject):
    '''Actualiza los datos del perfilador, en la propiedad data'''
    A = []
    serialObject.flushInput()
    serialObject.write(b"1")
    time.sleep(2)
    while True:
        if serialObject.inWaiting() == 0:
            break
        A.append(serialObject.read().decode())
    A = "".join(A)
    data = pd.read_csv(io.StringIO(A),sep="\t",names=["t","Vr", "Vc"])
    #data = data[np.isfinite(data["V"])]
    data = data.convert_objects(convert_numeric = True)
    return data.values

plt.close("all")
baudrate = 9600
port = inputPort()
ser = serial.Serial(port, baudrate)
data = update(ser)
plt.plot(data[:,0], data[:,1], 'ro-', data[:,0], data[:,2], 'go')
ser.close()