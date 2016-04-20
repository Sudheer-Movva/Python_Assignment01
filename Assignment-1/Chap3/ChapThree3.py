import math
#Atlanta
x1,y1 = 33.74, -84.38
#Orlando  
x2,y2 = 28.54, -81.38
#  Savannah
x3,y3 = 32.08, -81.09  
#Charlotte
x4,y4 = 35.23, -80.84

radius = 6371.01

d1 = radius * math.acos(math.sin(math.radians(x1)) * math.sin(math.radians(x2)) +
      math.cos(math.radians(x1)) * math.cos(math.radians(x2)) * 
      math.cos(math.radians(y1 - y2)));

d2 = radius * math.acos(math.sin(math.radians(x1)) * math.sin(math.radians(x3)) +
      math.cos(math.radians(x1)) * math.cos(math.radians(x3)) * 
      math.cos(math.radians(y1 - y3)));

d3 = radius * math.acos(math.sin(math.radians(x2)) * math.sin(math.radians(x3)) +
      math.cos(math.radians(x2)) * math.cos(math.radians(x3)) * 
      math.cos(math.radians(y2 - y3)));


s1 = (d1 + d2 + d3)/2
area1 = (s1*(s1-d1)*(s1-d2)*(s1-d3))** 0.5

d4 = radius * math.acos(math.sin(math.radians(x1)) * math.sin(math.radians(x4)) +
      math.cos(math.radians(x1)) * math.cos(math.radians(x4)) * 
      math.cos(math.radians(y1 - y4)));
      
d5 = radius * math.acos(math.sin(math.radians(x4)) * math.sin(math.radians(x3)) +
      math.cos(math.radians(x4)) * math.cos(math.radians(x3)) * 
      math.cos(math.radians(y3 - y4)));


s2 = (d2 + d4 + d5)/2
area2 = (s2*(s2-d2)*(s2-d4)*(s2-d5))** 0.5
totalArea = area1+area2

print("The total Area formed is :" , str(format((totalArea),"0.2f")))