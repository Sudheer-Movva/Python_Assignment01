from tkinter import *

class Panel:
    def __init__(self):
        window1 = Tk()
        window1.title("Moving Ball")
        self.canvas1 = Canvas(window1, width=200,height=100,bg="white")
        self.canvas1.pack()
        
        frame1 = Frame(window1)
        frame1.pack()
        buttonLeft = Button(frame1,text="Left",command=self.moveLeft())
        buttonRight = Button(frame1,text="Right",command=self.moveRight())
        buttonUp = Button(frame1,text="Up",command=self.moveUp())
        buttonDown = Button(frame1,text="Down",command=self.moveDown())

        buttonLeft.grid(row=1,column=1)
        buttonRight.grid(row=1,column=2)
        buttonUp.grid(row=1,column=3)
        buttonDown.grid(row=1,column=4)
        
        self.canvas1.create_oval(40, 40, 60, 60, outline='black', fill='gray40', tags="circle")
        window1.mainloop()
        
    def moveLeft(self):
        self.canvas1.move("circle",30,30)
        print(self.canvas1.coords("circle"))
                
    def moveRight(self):
        self.canvas1.move("circle",50,50)
                    
    def moveUp(self):
        self.canvas1.move("circle",10,10)
                    
    def moveDown(self):
        self.canvas1.move("circle",60,60)
        
Panel()
    