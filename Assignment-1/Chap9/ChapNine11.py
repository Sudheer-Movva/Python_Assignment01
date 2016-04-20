from tkinter import *
import datetime

'''
1. Get the current time
2. draw a oval
3. draw a 4 texts ; 
4. draw 3 lines ; length & direction
5. hours : 360/12 = 30, lowest in size
6. minutes: 360/60 = 6, medium in size 
7. seconds: 360/60 = 6, highest in size


'''
window = Tk()
window.title("Current Time")

canvas1 = Canvas(window,height=200,width=200)
canvas1.pack()

canvas1.create_oval(20,20,160,160)
current_time = datetime.datetime.strftime(datetime.datetime.now(), '%H:%M:%S')
canvas1.create_text(100,170,text=current_time)

window.mainloop()