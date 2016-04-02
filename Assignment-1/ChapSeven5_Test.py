import ChapSeven5

my_polygon = ChapSeven5.RegularPolygon(6,4)
print("Perimeter of hexagon with side as 4 is: ",my_polygon.getPerimeter())
print("Area of hexagon with side as 4 is: ",round(my_polygon.getArea(),3))

my_polygon = ChapSeven5.RegularPolygon(10,4,5.6,7.8)
print("Perimeter of regular decagon with side as 4 is: ",my_polygon.getPerimeter())
print("Area of regular decagon with side as 4 is: ",round(my_polygon.getArea(),3))
