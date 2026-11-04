import random
import sys
from pathlib import Path

# Para importar las cosas (¡¿Por qué es tan complicado en Python?!)
root_dir = Path(__file__).resolve().parents[2]    # Para cosas en ALGO
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))

import Lógica.variables
from Lógica.Registros.log import log

rangos_variables_aleatorias = Lógica.variables.rangos_variables_aleatorias

def generar_valores_de_variables_aleatorios(rangos_variables_aleatorias):
    log("Generando variables aleatorias.")

    variables_separadas = []
    for (minimo, maximo), decimales in rangos_variables_aleatorias:
        valor = round(random.uniform(minimo, maximo), decimales)
        variables_separadas.append(float(valor))
        log(variables_separadas)
        
    return variables_separadas

generar_valores_de_variables_aleatorios(rangos_variables_aleatorias)