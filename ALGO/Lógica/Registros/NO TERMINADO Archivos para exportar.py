import os
import json
import datetime
import sys
from pathlib import Path

# Para importar las cosas (¡¿Por qué es tan complicado en Python?!)
root_dir = Path(__file__).resolve().parents[2]    # Para cosas en ALGO
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))

import Lógica.Registros.log as log

directorio_archivos_exportados = "Archivos creados/Exportados/"
fecha = datetime.date.today().strftime("%Y-%m-%d")
ruta_JSON = os.path.join(directorio_archivos_exportados + fecha + ".JSON")
ruta_CSV = os.path.join(directorio_archivos_exportados + fecha + ".CSV")

# JSON

def crear_archivo_JSON(ruta_JSON):
    log(ruta_JSON)
    os.makedirs(ruta_JSON, exist_ok=True)
    
    if (os.path.exists(ruta_JSON) == True):
        log("El archivo JSON a exportar ya existía: " + ruta_JSON)
        with open(ruta_JSON, 'a') as file:
            file.write("")
            file.write("")
            file.write("")
            file.write("============================================")
            file.write("Empezando los registros de una nueva sesión.")
            file.write("============================================")
            file.write("")

    else:
        log("El archivo JSON a exportar se ha creado: " + ruta_JSON)
        with open(ruta_JSON, 'a') as file:
            file.write("=============================================")
            file.write("Empezando los registros de la primera sesión.")
            file.write("=============================================")
            file.write("")

### NO TERMINADO, HAY QUE HACER EL FORMATO ###
def mensaje_JSON(*args, sep=" "):
    linea_JSON = sep.join(str(arg) for arg in args)
    log(linea_JSON)
    escribir_archivo_JSON(linea_JSON)

def escribir_archivo_JSON(ruta_JSON, linea_JSON):
    with open(ruta_JSON, 'a') as file:
        file.write(linea_JSON)
    log("Se ha escrito al archivo JSON.")



# CSV

def crear_archivo_CSV(ruta_CSV):
    log(ruta_CSV)
    os.makedirs(ruta_CSV, exist_ok=True)
    
    if (os.path.exists(ruta_CSV) == True):
        log("El archivo CSV a exportar ya existía: " + ruta_CSV)
        with open(ruta_CSV, 'a') as file:
            file.write("")
            file.write("")
            file.write("")
            file.write("============================================")
            file.write("Empezando los registros de una nueva sesión.")
            file.write("============================================")
            file.write("")

    else:
        log("El archivo CSV a exportar se ha creado: " + ruta_CSV)
        with open(ruta_CSV, 'a') as file:
            file.write("=============================================")
            file.write("Empezando los registros de la primera sesión.")
            file.write("=============================================")
            file.write("")

### NO TERMINADO, HAY QUE HACER EL FORMATO ###
def mensaje_CSV(*args, sep=" "):
    linea_CSV = sep.join(str(arg) for arg in args)
    log(linea_CSV)
    escribir_archivo_CSV(linea_CSV)

def escribir_archivo_JSON(ruta_CSV, linea_CSV):
    with open(ruta_CSV, 'a') as file:
        file.write(linea_CSV)
    log("Se ha escrito al archivo CSV.")




