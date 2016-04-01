import turtle

turtle.pensize(2) 
turtle.penup()
turtle.goto(-120, -120)
turtle.pendown()
turtle.color("black")

for grid_square in range(0,4,1):
    turtle.forward(240) 
    turtle.left(90)

for y_axis in range(-120, 90, 60): 
    for x_axis in range(-120, 120, 60):
        turtle.penup()
        turtle.goto(x_axis, y_axis)
        turtle.pendown()
        turtle.begin_fill()
        for k in range(0,4,1):
            turtle.forward(30)
            turtle.left(90)
        turtle.end_fill()

for y_axis in range(-90, 120, 60): 
    for x_axis in range(-90, 120, 60):
        turtle.penup()
        turtle.goto(x_axis, y_axis)
        turtle.pendown()        
        turtle.begin_fill()
        for k in range(4):
            turtle.forward(30)
            turtle.left(90)
        turtle.end_fill()

turtle.hideturtle()
turtle.done()