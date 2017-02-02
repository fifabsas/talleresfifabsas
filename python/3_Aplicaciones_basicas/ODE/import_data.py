# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 18:48:58 2015

@author: Publico

Ver documentation en: http://docs.scipy.org/doc/numpy/reference/generated/numpy.loadtxt.html
                      http://pandas.pydata.org/pandas-docs/stable/generated/pandas.io.parsers.read_csv.html
"""

def leercsv(filename, skiplines=0):
    import numpy as np
    return np.loadtxt(filename, delimiter=',', skiprows=skiplines,
                      usecols=(),  unpack=True)
                      
def leertab(filename, skiplines=0):
    import numpy as np
    return np.loadtxt(filename, delimiter='\t', skiprows=skiplines,
                      usecols=(),  unpack=True)

def leertabcd(filename, nro_lin_encabez=0):
    result = []
    from pandas import read_csv
    import numpy as np
    # Leer el archivo, separado por tabulaciones, salteando 3 lineas de header
    #     y empleando la coma como separador decimal
    df = read_csv(filename, sep='\t', skiprows=nro_lin_encabez, decimal='.')
    # Convertir el dataframe de pandas a un array de numpy
    nparray = df.as_matrix()
    # Remover los posibles nans del archivo
    nparray = nparray[~np.isnan(nparray).any(axis=1)]
    # Asignar las columnas a variables de salida
    for cols in range(nparray.shape[1]):
        out = nparray[:,cols]
        result.append(out)

    return result
