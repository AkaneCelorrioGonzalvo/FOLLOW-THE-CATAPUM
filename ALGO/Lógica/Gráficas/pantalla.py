import turtle
import io
import base64
import math
import tkinter as tk
import sys
from pathlib import Path
from PIL import Image 


# Para importar las cosas (¡¿Por qué es tan complicado en Python?!😭)
root_dir = Path(__file__).resolve().parents[2]    # Para cosas en ALGO
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))

from Lógica.Registros.log import log
from Lógica.variables import *
from Lógica.Modos.Modo_prueba import generar_valores_de_variables_aleatorios
from Lógica.Datos.Agregar_al_diccionario import agregar_datos_numericos_al_diccionario

"""
if (Lógica.variables.modo_prueba == True):
    variables_separadas = generar_valores_de_variables_aleatorios(Lógica.variables.rangos_variables_aleatorias)
else:
    # variables_separadas = generar_valores_de_variables_aleatorios(Lógica.variables.rangos_variables_aleatorias)
    pass
"""

paso_del_angulo = 5         # Cada sprite rota 5º, creando 72 imágenes
angulo_inicial = 90         # Hacia dónde apunta el sprite inicialmente
tamaño_sprite = (80, 80)    # Para ajustar el tamaño del sprite

size = [700, 700]  # [ancho, alto], temporal. Creo que esto debería ser dinámico según los rangos de las variables
margen = 30
origin = (-size[0] / 2 + margen, -size[1] / 2 + margen)  # esquina inferior izquierda con margen

tema = "white" # Temporal, debe ser un argumento pasado desde un botón (o algo así)
tamaño_pantalla = (700, 700)

def actualizar_los_datos():
    log("Actualizando los datos.")
    
    if modo_prueba == True:
        generar_valores_de_variables_aleatorios()
        agregar_datos_numericos_al_diccionario()
    else:
        pass # Habría que ponerlo para que fuera lo del modo serial

    global datos_para_la_grafica
    datos_para_la_grafica = []
    for sensor in SENSORES_TELEMETRIA:
        datos_para_la_grafica.append({
            "clave": sensor["clave"],
            "valor": sensor["valor"],
            "minimo": sensor["minimo"],
            "maximo": sensor["maximo"]
    })
    log("Datos para la gráfica:", datos_para_la_grafica)

def cargar_sprites(screen, ruta):
    log("Cargando los sprites.")
    base = Image.open(ruta).convert("RGBA").resize(tamaño_sprite)
    log("Sprite cargado y cambiado de tamaño correctamente.")
    fotos = []  # guardamos las referencias para que Tk no las libere
    for ang in range(0, 360, paso_del_angulo):
        img = base.rotate(ang - angulo_inicial, expand=True, resample=Image.BICUBIC)

        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        datos = base64.b64encode(buffer.getvalue())

        foto = tk.PhotoImage(master=screen.getcanvas(), data=datos)
        fotos.append(foto)
        screen.register_shape(f"cohete_{ang}", turtle.Shape("image", foto))
        log("Sprite registrado correctamente.")
    return fotos

def orientar(cohete, x, y):
    x0, y0 = cohete.position()
    dx, dy = x - x0, y - y0
    log("Derivadas de los componentes X e Y:", dx, dy)
    if abs(dx) + abs(dy) < 0.01:      
        return
    ang = math.degrees(math.atan2(dy, dx)) % 360
    log("Ángulo calculado:", ang)
    ang_sprite = (round(ang / paso_del_angulo) * paso_del_angulo) % 360
    log("Ángulo del sprite:", ang_sprite)
    cohete.shape(f"cohete_{ang_sprite}")
    log("Ángulo del sprite cambiado correctamente.")

def crear_tortuga() -> turtle.Turtle:
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.penup()
    return t

def pintar_ejes():
    log("Pintando ejes de la gráfica.")

    x, y = (datos_para_la_grafica[0]["minimo"], datos_para_la_grafica[1]["minimo"])
    log("Coordenadas de X e Y actuales:", x, y)
    largo_x = round(datos_para_la_grafica[0]["maximo"] - 2 * margen)
    log("Largo de X:", largo_x)
    largo_y = round(datos_para_la_grafica[1]["maximo"] - 2 * margen)
    log("Largo de Y:", largo_y)

    eje = crear_tortuga()
    log("Eje creado:", eje)
    texto = crear_tortuga()
    log("Texto de los ejes:,", texto)

    # Eje X
    eje.goto(x, y)
    eje.pendown()
    eje.goto(x + largo_x, y)
    eje.penup()

    # Eje Y
    eje.goto(x, y)
    eje.pendown()
    eje.goto(x, y + largo_y)
    eje.penup()

    # Marcas en el eje X
    for i in range(0, largo_x + 1, 20):
        eje.goto(x + i, y - 5)
        eje.pendown()
        eje.goto(x + i, y + 5)
        eje.penup()
        texto.goto(x + i, y - 20)
        texto.write(i, align="center", font=("Arial", 8, "normal"))
        log("Marca en el eje X: ", x + i, y - 5)

    # Marcas en el eje Y
    for i in range(0, largo_y + 1, 20):
        eje.goto(x - 5, y + i)
        eje.pendown()
        eje.goto(x + 5, y + i)
        eje.penup()
        texto.goto(x - 10, y + i - 5)
        texto.write(i, align="right", font=("Arial", 8, "normal"))
        log("Marca en el eje Y: ", x - 5, y - i)


def inicializar_pantalla(tamaño_pantalla):
    actualizar_los_datos()

    log("Inicializando pantalla.")
    screen = turtle.Screen()
    screen.title("Gráfica del cohete: " + datos_para_la_grafica[0]["clave"]
                 + " respecto a " + datos_para_la_grafica[1]["clave"])
    log("Título de la gráfica:", screen.title)
    screen.bgcolor(tema)
    log("Tema escogido:", tema)
    screen.setup(width=tamaño_pantalla[0], height=tamaño_pantalla[1]) # Esto debería cambiar según el tamaño de la ventana, creo yo
    screen.tracer(0)

    fotos = cargar_sprites(screen, "ALGO/Recursos gráficos/Sprite/Artemisa II.gif")

    cohete = turtle.Turtle()
    cohete.shape("cohete_0")
    cohete.color("blue")
    cohete.penup()
    cohete.goto(origin)
    cohete.pendown()

    pintar_ejes()
    screen.update()
    log("Pantalla actualizada.")

    screen.tracer(0)
    screen.delay(0)
    cohete.speed(0)

    return screen, cohete, fotos

def trayectoria():
    x = datos_para_la_grafica[0]["valor"]
    log("Valor de X en la gráfica:", x)
    y = datos_para_la_grafica[1]["valor"]
    log("Valor de Y en la gráfica:", y)
    return (x, y)

def mover(screen, cohete, t=0):
    x, y = trayectoria()
    orientar(cohete, x, y)   
    cohete.goto(x, y)
    log("Cohete movido a:", x, y)      
    screen.update()
    log("Pantalla actualizada.")
    if t < size[0] - 60:
        screen.ontimer(lambda: mover(screen, cohete, t + 5), 20)

def actualizar_el_sprite(cohete, screen):
    actualizar_los_datos()
    log("Actualizando el sprite.")

    x, y = trayectoria()
    orientar(cohete, x, y)   
    cohete.goto(x, y)
    log("Cohete movido a:", x, y)      
    
    screen.update()
    log("Pantalla actualizada.")
    
    screen.ontimer(lambda: actualizar_el_sprite(cohete, screen), 250)
    log("Temporizador de pantalla completado.")


def main():
    log("Iniciando pantalla.")

    screen, cohete, fotos = inicializar_pantalla(size)
    actualizar_el_sprite(cohete, screen)
    screen.mainloop()

main()















































"""

import turtle
import time

# Nota: organizar mejor el codigo en funciones de generacion de la pantalla y
# funciones que se deban ejecutar en bucle para actualizar la grafica

size = [700, 700] # Componente 1 es de las X, componente 2 es de las Y
# Creo que esto se debería pasar como argumento para adaptar los ejes de una determinada gráfica

origin = (-(size[0]/2) + 30, -(size[1]/2) + 30) # ¿Y esto de dónde narices sale? ¿Por qué 30 y 40?

# Variables a usar no puestas:
# nombres_variables_grafica: Array con los nombres de las variables
# variables_grafica: Array con los valores recibidos de las variables
# maximos_variables_grafica: Array con los valores maximos que se hayan recibido hasta el momento. Para la dinamicidad de los ejes
# tema: blanco si el tema es claro, negro si el tema es oscuro


nombres_variables_grafica = ["algo", "algomas"]
tema = "white"

def crear_tortuga() -> turtle.Turtle:
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.penup()

    return t

def inicializar_pantalla(nombres_variables_grafica, size):
    screen = turtle.Screen()
    screen.title("Gráfica del cohete: " + nombres_variables_grafica[0] + " respecto a " + nombres_variables_grafica[1] )
    screen.bgcolor(tema)
    screen.setup(width=size[0], height=size[1])
    screen.tracer(0) # Se actualiza la pantalla manualmente

    screen.register_shape("artemisa.gif") # Para usar un sprite personalizado
    cohete = turtle.Turtle()
    cohete.shape("artemisa.gif")
    cohete.shapesize(0.05, 0.05) # ¿Para ajustar el tamaño del sprite? No parece funcionar
    cohete.speed(1) # ¿Esto se podría hacer variable, según los datos recibidos?
    cohete.color("blue") # Azul mejor :)
    cohete.penup()

    cohete.goto(origin)
    cohete.pendown()

    pintar_ejes()

    # Temporal
    screen.tracer(1) # Cambio para que se actualiza la pantalla a la velocidad predeterminada
    cohete.setheading(45)
    # Nota: Investigar mejor como ejecutar bucles para evitar errores al cerrar la ventana
    screen.ontimer(mover, 20)
    screen.mainloop()

    return cohete

def pintar_ejes(): # Esto hace que los ejes X e Y tengan el mismo tamaño, lo cual puede no ser conveniente. Los he cambiado para que sean dinámicos.
    x, y = origin
    
    eje = crear_tortuga()
    eje.goto(origin)
    eje.pendown()

    # Dibujar los ejes
    eje.goto(x, y)
    eje.pendown()
    eje.goto(x + size[0], y)

    eje.penup()
    eje.goto(x, y)
    eje.pendown()
    eje.goto(x, y + size[1])
    eje.penup()
    
    eje.penup()
    eje.goto(origin)
    eje.pendown()

    texto = crear_tortuga()

    for i in range(0, (size[0]), 20):
        eje.penup()
        eje.goto(x + i, y - 5)
        eje.pendown()
        eje.goto(x + i, y + 5)

        texto.goto(x + i, y - 20)
        texto.write(i, align="center", font=("Arial", 8, "normal"))

        eje.penup()
        eje.goto(x - 5, y + i)
        eje.pendown()
        eje.goto(x + 5, y + i)
        
        texto.goto(x - 20, y + i)
        texto.write(i, align="left", font=("Arial", 8, "normal"))

def mover(cohete): # Esto no es adaptable por el momento según los datos enviados por el cohete
    cohete.forward(10)
    screen.update()
    screen.ontimer(mover, 20)

crear_tortuga()
inicializar_pantalla(nombres_variables_grafica, size)

"""