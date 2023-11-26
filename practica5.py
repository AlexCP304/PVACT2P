# importaremos bibliotecas de tortugas de importacion de tortugas *, importar tortuga. los tortuga() metodo se utiliza para hacer objetos. dando click a la tortuga para moverla
from turtle import *
from turtle import Turtle, Screen

def drag(i, j): #mover la tortuga a una posicion abso
    tur.ondrag(None)#arrastrar el cursor y seguir el raton
    tur.setheading(tur.towards(i, j))
    tur.goto(i, j)
    tur.ondrag(drag)

ws = Screen()#hacer la pantalla
tur = Turtle('turtle')
tur.speed('fastest')#dar mayor velocidad a la tortuga
tur.ondrag(drag)

ws.mainloop()