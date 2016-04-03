import time

class Time:
    def __init__(self):
        total_seconds = int(time.time())
        self.__second = total_seconds % 60
        total_minutes = total_seconds // 60
        self.__minute = total_minutes % 60
        total_hours = total_minutes // 60
        self.__hour = total_hours % 24
    
    def getHour(self):
        return self.__hour
    
    def getMinute(self):
        return self.__minute
    
    def getSecond(self):
        return self.__second
    
    def setTime(self,elapsedTime):
        if int(elapsedTime) > 0:            
            total_seconds = int(elapsedTime)
            self.__second = total_seconds % 60
            total_minutes = total_seconds // 60
            self.__minute = total_minutes % 60
            total_hours = total_minutes // 60
            self.__hour = total_hours % 24
    