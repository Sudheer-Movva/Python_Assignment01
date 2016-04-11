
class GeometicObject():
    def __init__(self,color,filled):
        self.__color = color
        self.__filled = filled
        
    def getColor(self):
        return self.__color
    
    def getFilled(self):
        if self.__filled == 1:
            return True
        elif self.__filled == 0:
            return False
    
    
    def setColor(self,color):
        self.__color = color
        
    def setFilled(self,filled):
        self.__filled = filled
        

class Triangle(GeometicObject):
    def __init__(self,color,filled,side1=1.0,side2=1.0,side3=1.0):
        super().__init__(color,filled)
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3
    
    def getSide1(self):
        return self.__side1
    
    def getSide2(self):
        return self.__side2
    
    def getSide3(self):
        return self.__side3
    
    def getPerimeter(self):
        return (self.__side1 + self.__side2 + self.__side3)
    
    def getArea(self):
        side_cons = (self.__side1 + self.__side2 + self.__side3)/2
        area = round((side_cons*(side_cons - self.__side1)*(side_cons - self.__side2)*(side_cons - self.__side3)) ** 0.5,2)
        return area
        
    def __str__(self):
        return "Triangle: side1= " + str(self.__side1) + " side2 = " + str(self.__side2) + " side3 " + str(self.__side3)
     

s1,s2,s3 = eval(input("Enter the three sides of a triangle: "))  
color = input("Enter the color of a triangle: ")
filled = eval(input("Input 1 or 0 to indicate whether a triangle is filled: "))       


trgl1 = Triangle(color,filled,s1,s2,s3)

print("Triangle\'s area is ",trgl1.getArea())
print("Triangle\'s perimeter is ",trgl1.getPerimeter())
print("Triangle\'s color is ",trgl1.getColor())
print("Is the triangle filled: ",trgl1.getFilled())
