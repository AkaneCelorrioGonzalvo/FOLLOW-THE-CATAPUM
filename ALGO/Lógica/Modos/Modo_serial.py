import serial
import time
import sys
from pathlib import Path

# Para importar las cosas (¡¿Por qué es tan complicado en Python?!)
root_dir = Path(__file__).resolve().parents[2]    # Para cosas en ALGO
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))

import Lógica.Registros.log as log

def conexion_ESP32(puerto, baudios):
    log("Tratando de establecer la conexión incial.")

    conexion_serial = serial.Serial(puerto, baudios, timeout=1)
    time.sleep(2)
    log("Conexión serial establecida.")
    
    # Enviar un 'ping'
    ping = "Ping"
    conexion_serial.write(ping.encode('utf-8'))
    log("Ping enviado.")
    
    # Mirar a ver si se ha recibido un 'pong'
    pong = conexion_serial.readline().decode('utf-8').strip()
    log("Pong leído.")
    
    if (pong == "Pong"):
        log("Ping-pong completado.")
        leer_datos_ESP32()
    else:
        print("El ping-pong no he ha completado.")
        log(pong)
        log("Ping-pong no completado.")

def leer_datos_ESP32(conexion_serial, seguir_leyendo_datos):
    log("Tratando de leer los datos.")

    while True:
        texto = conexion_serial.readline().decode('utf-8').strip()
        log(texto)
        procesar_datos_ESP32(texto)
        time.sleep(0.25) # Para no petar la CPU
        if (seguir_leyendo_datos == False):
            log(seguir_leyendo_datos)
            break # Seguro que hay maneras más eficientes de hacer esto

def procesar_datos_ESP32(texto, numero_de_variables_emitidas):
    log("Tratando de procesar los datos.")

    global variables_separadas
    variables_separadas = texto.split(';')
    log(variables_separadas)

    for variable in variables_separadas:
        try:
            log(variable)
            variables_separadas.append(float(variable))
            if (len(variables_separadas) != numero_de_variables_emitidas):
                print("Error: se obtuvieron", {len(variables_separadas)}, "cuando se esperaban", {numero_de_variables_emitidas}, "variables.")
                log(variables_separadas)

            # Creo que esto comentado a continuación es innecesario, pues sería mejor que se reciban
            # las variables simplemente como un número, ¿no?
            
            # asignar_nombre_a_cada_variable_separada(variable, i)
            # i = i + 1


        except (ValueError, IndexError):
            print("Error: El mensaje no tiene el formato esperado o contiene datos corruptos.")
            log(variables_separadas)

    return variables_separadas

def asignar_nombre_a_cada_variable_separada(variable, i, listado_nombre_variables):
    # El formato era: acc_x;acc_y;acc_z;pitch;roll;yaw;vel;vel_max;latitud;longitud;altura;altura_max;temperatura;estado;flag

    #listado_nombre_variables[i] = float(variable)
    #log(listado_nombre_variables)

    # Hay que actualizar esto para que sea un diccionario
    