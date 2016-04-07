from tkinter import *

window1 = Tk()

canvas1 = Canvas(window1, width=200,height=100,bg="white")
canvas1.pack()

frame1 = Frame(window1)
frame1.pack()

def clearCanvas():
    #canvas1.delete("circle")
    canvas1.delete()

def moveLeft():
    clearCanvas()
    #canvas1.create_oval(40,40,50,50,fill="black",tags="circle")

def moveRight():
    clearCanvas()
    #canvas1.create_oval(40,40,50,50,fill="black",tags="circle")

def moveUp():
    clearCanvas()
    #canvas1.create_oval(40,30,50,40,fill="black",tags="circle")

def moveDown():
    clearCanvas()
    #canvas1.create_oval(40,30,50,40,fill="black",tags="circle")

buttonLeft = Button(frame1,text="Left",command=moveLeft())
buttonRight = Button(frame1,text="Right",command=moveRight())
buttonUp = Button(frame1,text="Up",command=moveUp())
buttonDown = Button(frame1,text="Down",command=moveDown())

buttonLeft.grid(row=1,column=1)
buttonRight.grid(row=1,column=2)
buttonUp.grid(row=1,column=3)
buttonDown.grid(row=1,column=4)

canvas1.create_oval(40,40,50,50,fill="black",tags="circle")

window1.mainloop()