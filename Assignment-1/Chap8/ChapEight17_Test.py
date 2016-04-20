import ChapEight17

x1,y1,x2,y2 = eval(input("Enter two points: "))

Point1 = ChapEight17.Point(x1,y1)


print("The distance between the two points is ", Point1.distance(x2, y2))

if Point1.isNearBy(x2, y2):
    print("The two points are near to each other")
else:
    print("The two points are not near to each other")
