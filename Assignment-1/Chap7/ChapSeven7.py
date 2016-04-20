
class LinearEquation:
    def __init__(self,a,b,c,d,e,f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f
        
    def getA(self):
        return self.__a
    
    def getB(self):
        return self.__b
    
    def getC(self):
        return self.__c
    
    def getD(self):
        return self.__d
    
    def getE(self):
        return self.__e
    
    def getF(self):
        return self.__f
    
    def isSolvable(self):
        if (self.__a * self.__d) - (self.__b * self.__c) != 0:
            return True
        else:
            return False
        
    def getX(self):
        if self.isSolvable():
            self.__x = ((self.__e)*(self.__d) - (self.__b*self.__f)) / ((self.__a*self.__d) - (self.__b*self.__c))
            return self.__x
        else:
            print("The equation has no solution")
    
    def getY(self):
        if self.isSolvable():
            self.__y = ((self.__a)*(self.__f) - (self.__e*self.__c)) / ((self.__a*self.__d) - (self.__b*self.__c))
            return self.__y
        else:
            print("The equation has no solution")
    
        