def main():
    x1,y1,x2,y2 = eval(input("Enter two points x1, y1, x2, y2: "))
    p2 = Point(x2,y2)
    p1 = Point(x1,y1)
    distance = p2.distance(p1)
    print("The distance between the two points is: "+format(distance,"0.2f"))
    if(p2.isNearBy(p1)):
        print("The two points are near each other")
    else:
        print("The two points are not near each other")
    
    #print(p1)
    
class Point():
    def __init__(self,x=0.0,y=0.0):
        self.__x= x
        self.__y =y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self, value):
        self.__x = value

    def set_y(self, value):
        self.__y = value

    def distance(self,p1):
        distance = ((self.__y-p1.get_y())**2+(self.__x-p1.get_x())**2)**0.5
        return distance
    
    def isNearBy(self,p1):
        if(self.distance(p1)>5):
            return False
        else:
            return True
    
    def __str__(self,p1):
        return str("(") + str(p1.get_x()) + str(",") + str(p1.get_y()) + str(")")
       
main()