import serial
import time
import Lógica.Procesar_datos as Procesar_datos

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
        print(f"error de serial {e}")
    except FileNotFoundError:
        print("File not found error")
    except PermissionError:
        print("Permision error")

if __name__ == "__main__":
    print(Procesar_datos.leer_datos_esp32_prueba())