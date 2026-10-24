import serial
from serial.tools import list_ports

def listar_puertos() -> list[dict]:
    puertos = []
    for puerto in list_ports.comports():
        puertos.append({"name": puerto.name, "descripción": puerto.description, "hwid": puerto.hwid,})

    return puertos

def recibir_datos(port: str):
    pass

if __name__ == "__main__":
    print(listar_puertos())