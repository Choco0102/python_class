
import turtle

win = turtle.Screen()
turtle.setup(800, 600)
turtle.title('산길 거북이')
win.bgpic('산길.gif')

t = turtle.Turtle('turtle')

t.penup()
t.goto(-100, -250)
t.left(30)
t.forward(200)
t.setheading(900)
t.forward(10)
t.setheading(150)
t.forward(100)

turtle.mainloop()