import turtle

x1,y1,r1 = eval(input("Enter circle1's center x-,y-coordinates, and radius: "))
x2,y2,r2 = eval(input("Enter circle2's center x-,y-coordinates, and radius: "))

distance_centers = ((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1)) ** 0.5
print("Distance between centers is: ",distance_centers)

if distance_centers <= abs(r1-r2):
    write_canvas = "Circle2 is inside Circle1"
elif distance_centers <= (r1+r2):
    write_canvas = "Circle2 overlaps Circle1"
else:
    write_canvas = "Circle2 doesnot overlap Circle1"

turtle.showturtle()

turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
turtle.circle(r1)

turtle.penup()
turtle.goto(x2,y2)
turtle.pendown()
turtle.circle(r2)
turtle.penup()
turtle.setx(x2+30)
turtle.pendown()
turtle.pensize(50)
turtle.write(write_canvas)

turtle.hideturtle()
turtle.done()