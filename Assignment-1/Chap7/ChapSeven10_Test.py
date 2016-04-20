import ChapSeven10
import time

current_time = ChapSeven10.Time()
print(time.time())
print("Current time is: ",current_time.getHour(),":",current_time.getMinute(),":",current_time.getSecond() )

elapsed_time = eval(input("Enter the elapsed time: "))
current_time.setTime(elapsed_time)
print("The hour:minute:second for the elapsed time is: ",current_time.getHour(),":",\
                                                        current_time.getMinute(),":",current_time.getSecond() )
