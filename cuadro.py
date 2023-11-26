import turtle


turtle.shape('turtle')


turtle.forward(0)


turtle.color('red', 'yellow')
turtle.begin_fill()
grados = 0
turtle.speed(15)
for x in range(1, 31):
      for x in range(0, 4):
        turtle.forward(100)
        turtle.left(90)
      turtle.left(grados + 10)
turtle.end_fill()
turtle.done()