DATOS = [4,6,8] 
#DATOS [5.0,6.0,8.0]

def F_media(lista):
    suma =0
    for numero in lista:
        suma += numero
    media = suma/len(lista)
    return media
    
print F_media(DATOS)





def F_varianza(lista):
    media_lista = F_media(lista)

    suma = 0
    for numero in lista:
        suma += (numero - media_lista )**2
    varianza = suma / len(lista)
    return varianza
    
print F_varianza(DATOS)
