import turtle

turtle.showturtle()

turtle.penup()
turtle.goto(-150,200)
turtle.pendown()
turtle.write("Cool Color Shapes")
turtle.penup()

turtle.penup()
turtle.goto(-150,50)
turtle.pendown()
turtle.begin_fill()
turtle.color("red")
turtle.setheading(60)
turtle.circle(50,steps=3)
turtle.end_fill()

turtle.penup()
turtle.goto(-40,50)
turtle.pendown()
turtle.begin_fill()
turtle.color("green")
turtle.setheading(45)
turtle.circle(50,steps=4)
turtle.end_fill()

turtle.penup()
turtle.goto(70,50)
turtle.pendown()
turtle.begin_fill()
turtle.color("yellow")
turtle.setheading(36)
turtle.circle(50,steps=5)
turtle.end_fill()



turtle.penup()
turtle.goto(180,50)
turtle.pendown()
turtle.begin_fill()
turtle.color("brown")
turtle.setheading(30)
turtle.circle(50,steps=6)
turtle.end_fill()

turtle.penup()
turtle.goto(290,50)
turtle.pendown()
turtle.begin_fill()
turtle.color("black")
turtle.setheading(22.5)
turtle.circle(50,steps=8)
turtle.end_fill()

turtle.hideturtle()
turtle.done()