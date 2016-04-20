import turtle
x1,y1,l,b = eval(input("Enter the center, width and height: "))

turtle.showturtle()

turtle.penup()
turtle.goto((x1+(b/2)),y1)
turtle.pendown()
turtle.forward(l/2)
turtle.right(90)
turtle.forward(b)
turtle.right(90)
turtle.forward(l)
turtle.right(90)
turtle.forward(b)
turtle.right(90)
turtle.forward(l/2)
turtle.hideturtle()
turtle.done()
