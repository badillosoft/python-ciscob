import turtle
from turtle import Turtle

t1 = Turtle()
t2 = Turtle()

t1.speed(1)

t1.color("red")
t2.color("#0863FF")

t1.fill(True)
for i in range(6):
    t1.forward(100)
    t1.left(60)
t1.fill(False)

t2.left(60)

t2.forward(100)

turtle.mainloop()