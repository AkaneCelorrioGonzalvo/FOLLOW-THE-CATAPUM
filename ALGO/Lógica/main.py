cargar_interfaz()

if (modo_prueba == False):
    conexion_ESP32()
    procesar_datos_ESP32()
else:
    conexion_prueba()
    procesar_datos_prueba()