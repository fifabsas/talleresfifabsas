import visa
import numpy as np

class Lockin(object):
    '''Clase para el manejo amplificador Lockin SR830 usando PyVISA de interfaz'''
    
    def __init__(self,resource):
        self._lockin = visa.ResourceManager().open_resource(resource)
        self._lockin.query('*IDN?')
        self._lockin("LOCL 2") #Bloquea el uso de teclas del Lockin
        
    def __del__(self):
        self._lockin("LOCL 0") #Desbloquea el Lockin
        self._lockin.close()
        
    def setModo(self, modo):
        '''Selecciona el modo de medición, A, A-B, I, I(10M)'''
        self._lockin.write("ISRC {0}".format(modo))
        
    def setFiltro(self, sen, tbase, slope):
        '''Setea el filtro de la instancia'''
        #Página 90 (5-4) del manual
        self._lockin.write("OFLS {0}".format(slope))
        self._lockin.write("OFLT {0}".format(tbase)) 
        self._lockin.write("SENS {0}".format(sen)) 
        
    def setAuxOut(self, auxOut = 1, auxV = 0):
        '''Setea la tensión de salida de al Aux Output indicado.
        Las tensiones posibles son entre -10.5 a 10.5'''
        self._lockin.write('AUXV {0}, {1}'.format(auxOut, auxV))
            
    def setReferencia(self,isIntern, freq, vRef = 1):
        if isIntern:
            #Referencia interna
            #Configura la referencia si es así
            self._lockin.write("FMOD 1")
            self._lockin.write("SLVL {0:f}".format(voltaje))
            self._lockin.write("FREQ {0:f}".format(freq))
        else:
            #Referencia externa
            self._lockin.write("FMOD 0")
            
    def setDisplay(self, isXY):
        if isXY:
            self._lockin.write("DDEF 1, 0") #Canal 1, x
            self._lockin.write('DDEF 2, 0') #Canal 2, y
        else:
            self._lockin.write("DDEF 1,1") #Canal 1, R
            self._lockin.write('DDEF 2,1') #Canal 2, T
    
    def getDisplay(self):
        '''Obtiene la medición que acusa el display. 
        Es equivalente en resolución a la medición de los parámetros con SNAP?'''
        orden = "SNAP? 10, 11"
        return self._lockin.query_ascii_values(orden, separator=",")
        
    def getMedicion(self,isXY = True):
        '''Obtiene X,Y o R,Ang, dependiendo de isXY'''
        orden = "SNAP? "
        if isXY:
            self._lockin.write("DDEF 1,0") #Canal 1, XY
            orden += "1, 2" #SNAP? 1,2
        else:
            self._lockin.write("DDEF 1,1") #Canal 1, RTheta
            orden += "3, 4" #SNAP? 3, 4
        return self._lockin.query_ascii_values(orden, separator=",")
        
        

class Osciloscopio(object):
    '''Clase para el manejo osciloscopio TDS2000 usando PyVISA de interfaz'''
    def __init__(self,resource):
	#Defino el recurso
        self._osci = visa.ResourceManager().open_resource(resource)
        self._osci.query("*IDN?")

	#Configuración de curva
        self._osci.write('DAT:ENC RPB') # Modo de transmision: Binario positivo. 
        self._osci.write('DAT:WID 1') #1 byte de dato. Con RPB 127 es la mitad de la pantalla
        self._osci.write("DAT:STAR 1") #La curva mandada inicia en el primer dato
        self._osci.write("DAT:STOP 2500") #La curva mandada finaliza en el último dato


        #Adquisición por sampleo
        self._osci.write("ACQ:MOD SAMP")
		
        #Seteo de canal
        self.setCanal(canal = 1, escala = 20e-3)
        self.setCanal(canal = 2, escala = 20e-3)
        self.setTiempo(escala = 1e-3, cero = 0)
		
        #Bloquea el control del osciloscopio
        self._osci.write("LOC")

    def __del__(self):
        self._osci.write("UNLOC") #Desbloquea el control del osciloscopio
        self._osci.close()

    def setCanal(self, canal, escala, cero = 0):
	#if coup != "DC" or coup != "AC" or coup != "GND":
	    #coup = "DC"
	#self._osci.write("CH{0}:COUP ".format(canal) + coup) #Acoplamiento DC
	#self._osci.write("CH{0}:PROB 
        print
        self._osci.write("CH{0}:SCA {1}".format(canal,escala))
        self._osci.write("CH{0}:POS {1}".format(canal,cero))
	
    def getCanal(self,canal):
        return self._osci.query("CH{0}?".format(canal))
		
    def setTiempo(self, escala, cero = 0):
        self._osci.write("HOR:SCA {0}".format(escala))
        self._osci.write("HOR:POS {0}".format(cero))	
	
    def getTiempo(self):
        return self._osci.query("HOR?")
	
    def getVentana(self,canal):
        self._osci.write("SEL:CH{0} ON".format(canal)) #Hace aparecer el canal en pantalla. Por si no está habilitado
        self._osci.write("DAT:SOU CH{0}".format(canal)) #Selecciona el canal
	#xze primer punto de la waveform
	#xin intervalo de sampleo
	#ymu factor de escala vertical
	#yoff offset vertical
        xze, xin, yze, ymu, yoff = self._osci.query_ascii_values('WFMPRE:XZE?;XIN?;YZE?;YMU?;YOFF?;', 
                                                                 separator=';') 
        data = (self._osci.query_binary_values('CURV?', datatype='B', 
                                               container=np.array) - yoff) * ymu + yze        
        tiempo = xze + np.arange(len(data)) * xin
        return tiempo, data
