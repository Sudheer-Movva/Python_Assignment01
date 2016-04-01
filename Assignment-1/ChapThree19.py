import turtle

x1,y1,x2,y2 = eval(input("Enter two points: "))

turtle.showturtle()

turtle.pensize(1.5)
turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
turtle.write("("+str(x1)+","+str(y1)+")")
turtle.goto(x2,y2)
turtle.penup()
turtle.goto(x2-10,y2-10)
turtle.write("("+str(x2)+","+str(y2)+")")

turtle.hideturtle()
turtle.done()
