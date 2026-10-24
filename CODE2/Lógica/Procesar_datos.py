import random

from Config_sensores import (SENSORES_TELEMETRIA, CLAVES_SENSORES_TELEMETRIA)


"""
    Pide un dato y lo procesa:
    - convierte el mensaje recibido a diccionario
    - guarda muestra en JSONL
    - añade muestra al registro
    - actualiza sensores de la interfaz

    Formato recomendado:
        acc_x;acc_y;acc_z;pitch;roll;yaw;vel;vel_max;latitud;longitud;altura;altura_max;temperatura;estado;flag\n

    También acepta JSON tipo diccionario con las mismas claves.

    Devuelve:
        {
            "ok": True/False,
            "tipo_error": None / "sin_datos" / "formato" / "guardado",
            "muestra": dict | None
        }
"""

def convertir_valor(valor: str, tipo: str):
    texto = valor.strip().replace(",", ".")
    
    if tipo == "int":
        return int(texto)
    
    if tipo == "byte":
        return max(0, min(255, texto))
    
    if tipo == "bool":
        return bool(int(float(texto)))

    if tipo == "str":
        return valor

    return float(texto)

def convertir_texto_de_puntocoma(texto: str) -> dict:
    salida: dict = {}
    valores: list[str] = [valor.strip() for valor in texto.split(";")]

    if valores and valores[-1] == "":
        valores = valores[:-1]

    valores_esperdos = len(SENSORES_TELEMETRIA)

    if len(valores) != valores_esperdos:
        # Pensar en como dar el error de menos datos de los esperados
        pass

    for index, clave_valor in enumerate(SENSORES_TELEMETRIA):
        salida[clave_valor["clave"]] = convertir_valor(valores[index], clave_valor["tipo_variable"])

    return salida

def leer_datos_esp32_prueba():
    """
    Simula una lectura del ESP32.

    Devuelve una línea con los 15 sensores separados por ';'.
    """

    valores = [
        round(random.uniform(-16, 16), 3),       # acc_x [G]
        round(random.uniform(-16, 16), 3),       # acc_y [G]
        round(random.uniform(-16, 16), 3),       # acc_z [G]
        round(random.uniform(-180, 180), 2),     # pitch [°]
        round(random.uniform(-180, 180), 2),     # roll [°]
        round(random.uniform(0, 360), 2),        # yaw [°]
        round(random.uniform(0, 250), 2),        # vel [m/s]
        round(random.uniform(0, 300), 2),        # vel_max [m/s]
        round(random.uniform(-90, 90), 6),       # latitud [°]
        round(random.uniform(-180, 180), 6),     # longitud [°]
        round(random.uniform(0, 3000), 2),       # altura [m]
        round(random.uniform(0, 5000), 2),       # altura_max [m]
        round(random.uniform(-20, 80), 1),       # temperatura [°C]
        random.randint(0, 10),                   # estado
        random.randint(0, 255),                  # flag
    ]

    return ";".join(str(valor) for valor in valores) + "\n"