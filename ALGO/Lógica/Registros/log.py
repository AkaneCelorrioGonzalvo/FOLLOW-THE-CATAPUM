import datetime
import os
import sys
from pathlib import Path

# Para importar las cosas (¡¿Por qué es tan complicado en Python?!)
root_dir = Path(__file__).resolve().parents[2]    # Para cosas en ALGO
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))

import Lógica.variables

log_visibilidad = True # por el momento lo dejo fijo

directorio_registros = "Archivos creados/Registros/"
fecha = datetime.date.today().strftime("%Y-%m-%d")
ruta_registros = os.path.join(directorio_registros, "registros_" + fecha + ".txt")

def encabezado_archivo_de_registros(ruta_registros):
    os.makedirs(directorio_registros, exist_ok=True)
    
    if (os.path.exists(ruta_registros) == True):
        with open(ruta_registros, 'a') as file:
            file.write("\n")
            file.write("\n")
            file.write("\n")
            file.write("============================================\n")
            file.write("Empezando los registros de una nueva sesión.\n")
            file.write("============================================\n")
            file.write("\n")

    else:
        with open(ruta_registros, 'a') as file:
            file.write("=============================================\n")
            file.write("Empezando los registros de la primera sesión.\n")
            file.write("=============================================\n")
            file.write("\n")

def log(*args, sep=" "):
    encabezado_archivo_de_registros(ruta_registros)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mensaje = sep.join(str(arg) for arg in args)
    mensaje_con_tiempo = "[" + timestamp + "]" + " " + mensaje + "\n"
    
    if(log_visibilidad == True):
        print(mensaje_con_tiempo)
    
    escribir_en_archivo_de_registros(ruta_registros, mensaje_con_tiempo)

def escribir_en_archivo_de_registros(ruta_registros, mensaje_con_tiempo):
    with open(ruta_registros, 'a') as file:
        file.write(mensaje_con_tiempo)
        file.write()



