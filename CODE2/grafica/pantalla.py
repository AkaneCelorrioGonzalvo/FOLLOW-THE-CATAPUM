import turtle
import time

# Nota: organizar mejor el codigo en funciones de generacion de la pantalla y
# funciones que se deban ejecutar en bucle para actualizar la grafica

size = 700
origin = (-(size/2) + 30, -(size/2) + 40)

def crear_tortuga() -> turtle.Turtle:
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.penup()

    return t

def pintar_ejes():
    x, y = origin
    
    eje = crear_tortuga()
    eje.goto(origin)
    eje.pendown()

    # Dibujar los ejes
    eje.goto(x, y)
    eje.pendown()
    eje.goto(x + size, y)

    eje.penup()
    eje.goto(x, y)
    eje.pendown()
    eje.goto(x, y + size)
    eje.penup()
    
    eje.penup()
    eje.goto(origin)
    eje.pendown()

    texto = crear_tortuga()

    for i in range(0, size, 20):
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

def mover():
    cohete.forward(10)
    screen.update()
    screen.ontimer(mover, 20)

# inicialización de la pantalla
screen = turtle.Screen()
screen.title("Gráfica del cohete")
screen.bgcolor("white")
screen.setup(width=size, height=size)
screen.tracer(0) # Se actualiza la pantalla manualmente

cohete = turtle.Turtle()
cohete.shape("turtle")
cohete.shapesize(0.5, 0.5)
cohete.speed(1)
cohete.color("green")
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