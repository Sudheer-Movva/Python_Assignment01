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
turtle.color("blue")
turtle.penup()

for x in range(-175, 176):
    turtle.goto(x, 50 * math.sin((x / 100) * 2 * math.pi))
    turtle.pendown()

turtle.penup()
turtle.goto(-100,-15)
turtle.color("black")
turtle.write("2\u03c0")

turtle.penup()
turtle.color("red")

for x in range(-175, 176):
    turtle.goto(x, 50 * math.cos((x / 100) * 2 * math.pi))
    turtle.pendown()

turtle.penup()
turtle.goto(100,-15)
turtle.color("black")
turtle.write("2\u03c0")


turtle.hideturtle()
turtle.done()