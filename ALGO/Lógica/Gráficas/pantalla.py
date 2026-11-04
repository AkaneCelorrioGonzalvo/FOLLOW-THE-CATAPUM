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

# from Lógica.Registros.log import log

lazy import Lógica.variables
lazy from Lógica.Modos.Modo_prueba import generar_valores_de_variables_aleatorios
# lazy from Modos.Modo_serial import 

if (Lógica.variables.modo_prueba == True):
    variables_separadas = generar_valores_de_variables_aleatorios(Lógica.variables.rangos_variables_aleatorias)
else:
    # variables_separadas = generar_valores_de_variables_aleatorios(Lógica.variables.rangos_variables_aleatorias)
    pass


paso_del_angulo = 5         # Cada sprite rota 5º, creando 72 imágenes
angulo_inicial = 90         # Hacia dónde apunta el sprite inicialmente
tamaño_sprite = (80, 80)    # Para ajustar el tamaño del sprite

variables_grafica = variables_separadas[0, 1]
size = [700, 700]  # [ancho, alto], temporal. Creo que esto debería ser para el tamaño de la ventana
margen = 30
origin = (-size[0] / 2 + margen, -size[1] / 2 + margen)  # esquina inferior izquierda con margen

nombres_variables_grafica = ["algo", "algomas"] # Temporal
tema = "white" # Temporal, debe ser un argumento pasado desde un botón (o algo así)


def cargar_sprites(screen, ruta):
    base = Image.open(ruta).convert("RGBA").resize(tamaño_sprite)
    fotos = []  # guardamos las referencias para que Tk no las libere
    for ang in range(0, 360, paso_del_angulo):
        img = base.rotate(ang - angulo_inicial, expand=True, resample=Image.BICUBIC)

        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        datos = base64.b64encode(buffer.getvalue())

        foto = tk.PhotoImage(master=screen.getcanvas(), data=datos)
        fotos.append(foto)
        screen.register_shape(f"cohete_{ang}", turtle.Shape("image", foto))
    return fotos

def orientar(cohete, x, y):
    x0, y0 = cohete.position()
    dx, dy = x - x0, y - y0
    if abs(dx) + abs(dy) < 0.01:      
        return
    ang = math.degrees(math.atan2(dy, dx)) % 360
    ang_sprite = (round(ang / paso_del_angulo) * paso_del_angulo) % 360
    cohete.shape(f"cohete_{ang_sprite}")

def crear_tortuga() -> turtle.Turtle:
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.penup()
    return t

def pintar_ejes():
    x, y = origin
    largo_x = size[0] - 2 * margen
    largo_y = size[1] - 2 * margen

    eje = crear_tortuga()
    texto = crear_tortuga()

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

    # Marcas en el eje Y
    for i in range(0, largo_y + 1, 20):
        eje.goto(x - 5, y + i)
        eje.pendown()
        eje.goto(x + 5, y + i)
        eje.penup()
        texto.goto(x - 10, y + i - 5)
        texto.write(i, align="right", font=("Arial", 8, "normal"))


def inicializar_pantalla(nombres_variables_grafica, size):
    screen = turtle.Screen()
    screen.title("Gráfica del cohete: " + nombres_variables_grafica[0]
                 + " respecto a " + nombres_variables_grafica[1])
    screen.bgcolor(tema)
    screen.setup(width=size[0], height=size[1]) # Esto debería cambiar según el tamaño de la ventana, creo yo
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

    screen.tracer(0)
    screen.delay(0)
    cohete.speed(0)

    return screen, cohete, fotos

def trayectoria(variables_grafica):
    x = variables_grafica[0]
    y = variables_grafica[1]
    return (x, y)

def mover(screen, cohete, t=0):
    x, y = trayectoria(t)
    orientar(cohete, x, y)   
    cohete.goto(x, y)      
    screen.update()
    if t < size[0] - 60:
        screen.ontimer(lambda: mover(screen, cohete, t + 5), 20)


screen, cohete, fotos = inicializar_pantalla(nombres_variables_grafica, size)
mover(screen, cohete)
screen.mainloop()
















































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