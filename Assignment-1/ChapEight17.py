
class Point:
    def __init__(self,x=0,y=0):
        self.__x = x
        self.__y = y
        
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def distance(self,x1,y1):
        dist = ((self.__x-x1)*(self.__x-x1) + (self.__y-y1)*(self.__y-y1)) ** 0.5
        return round(dist,2)
    
    def isNearBy(self,x1,y1):
        if self.distance(x1, y1) < 5:
            return True
        else:
            return False
        
    