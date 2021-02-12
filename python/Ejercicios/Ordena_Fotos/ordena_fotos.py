# Traigo una libreria que me va a permitir mover las imagenes
# y realizar operaciones en archivos
#
# Pueden traer otras librerias, todas las que quieran.
# No es necesario que usen solamente la que les proponemos nosotros
import os

# Me armo mi diccionario con las fechas de referencia y los nombres de las carpetas
fechas_lugares = {  "20210203" : "SantaFe",
                    "20210117" : "Chubut",
                    "20200630" : "Salta",
                    "20200513" : "Misiones",
                    "20201210" : "Catamarca",
                    "20200929" : "Mendoza"
                 }

for nombre_img in os.listdir("imagenes"):
    # Aca recorro cada una de las imagenes de la carpeta "imagenes" y guardo su
    # nombre en la variable nombre_img
    # Les dejamos una posibilidad de pasos a seguir para lograr nuestro cometido:
    # 1. Averiguar la fecha de la foto

    # 2. Determinar la carpeta apropiada de la imagen

    # 3. Mover la imagen a la carpeta encontrada.

