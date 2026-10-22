import serial, serial.tools.list_ports
import time

def prueba_de_conexion(port, baudRate = 115200):
    try:
        #Inicializar la conexión
        ser = serial.Serial(port=port, baudrate=baudRate, timeout=2)
        time.sleep(1) #waiting for device init

        #Enviar un mensaje
        ser.write(b"ENCENDER") #La b para enviarlo en forma de bytes
        #Recibir respuesta del dispositivo
        respuesta = ser.readline()

        #Mostrar el mensaje
        print(f"respuesta: {respuesta.decode('utf-8').strip()}") #El decode se usa para decodificar en mensaje que se recive en bytes

        #Cerrar la conexion al acabar la interacción
        ser.close()

    #Errores
    except serial.SerialException as e:
        print("error de serial {e}")
    except FileNotFoundError:
        print("File not found error")
    except PermissionError:
        print("Permision error")

#Ver todos los puertos del ordenador
for port in serial.tools.list_ports.comports():
    print(f"{port.device}: {port.description}")

prueba_de_conexion('COM1')