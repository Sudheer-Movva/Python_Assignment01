import turtle
import math

turtle.showturtle()
turtle.screensize(500,500)
turtle.speed(10)
turtle.forward(200)
turtle.setheading(140)
turtle.forward(10)
turtle.penup()
turtle.goto(200,0)
turtle.setheading(-140)
turtle.pendown()
turtle.forward(10)
turtle.penup()
turtle.home()
turtle.pendown()
turtle.backward(200)
turtle.home()
turtle.left(90)
turtle.forward(200)
turtle.setheading(50)
turtle.backward(10)
turtle.penup()
turtle.goto(0,200)
turtle.setheading(-50)
turtle.pendown()
turtle.forward(10)
turtle.penup()
turtle.home()
turtle.right(90)
turtle.pendown()
turtle.forward(200)
turtle.home()
turtle.penup()

for x in range(-15, 16,1):
    turtle.goto(x, x*x)
    turtle.pendown()


turtle.hideturtle()
turtle.done()