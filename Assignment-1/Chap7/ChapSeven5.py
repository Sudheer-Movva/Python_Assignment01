import math

class RegularPolygon:
    def __init__(self,n=3,side=1,x=0,y=0):
        self.__n = n
        self.__side = float(side)
        self.__x = float(x)
        self.__y = float(y)
    
    def setNoofSides(self,n):
        self.__n = n
    
    def setSide(self,side):
        self.__side = side
    
    def setXCoordinate(self,x):
        self.__x = x
        
    def setYCoordinate(self,y):
        self.__y = y
    
        
    def getNoofSides(self,n):
        return self.__n
    
    def getSide(self,side):
        return self.__side
    
    def getXCoordinate(self,x):
        return self.__x
        
    def getYCoordinate(self,y):
        return self.__y
    
    def getPerimeter(self):
        return (self.__n)*(self.__side)
    
    def getArea(self):
        return (self.__n * self.__side * self.__side) / (4 * math.tan(math.pi / self.__n))
    