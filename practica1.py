# ejecuta la funcion punto() cada vez que se hace click en la ventana de tortuga. la funcion simplemente dibuja un punto en el lugar en el que se haga el click

from turtle import *
setup(450, 200, 0, 0)
screensize(300, 150)
title("PROGRAMACION VISUAL")
hideturtle()
penup()

def punto(x,y):
    goto(x, y)
    dot(10, "black")

onscreenclick(punto)
mainloop()