
x1,y1,r1 = eval(input("Enter circle1's center x-,y-coordinates, and radius: "))
x2,y2,r2 = eval(input("Enter circle2's center x-,y-coordinates, and radius: "))

distance_centers = ((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1)) ** 0.5
print("Distance between centers is: ",distance_centers)

if distance_centers <= abs(r1-r2):
    print("Circle2 is inside Circle1")
elif distance_centers <= (r1+r2):
    print("Circle2 overlaps Circle1")
else:
    print("Circle2 is completely outside Circle1")