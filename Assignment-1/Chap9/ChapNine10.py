from tkinter import *

class piechart():
    def __init__(self):
        window = Tk()
        window.title("Pie-Chart")
        
        self.canvas1 = Canvas(window, width=350,height=350,bg="white")
        self.canvas1.pack()
        
        
        self.canvas1.create_arc((50,50,198,198),fill="red",start=self.frac(0),extent=self.frac(20))
        self.canvas1.create_text(200,90,text="Project--20%",tags="proj")
        self.canvas1.create_arc((50,50,198,198),fill="blue",start=self.frac(20),extent=self.frac(10))
        self.canvas1.create_text(150,45,text="Quizzes--10%",tags="quiz")
        self.canvas1.create_arc((50,50,198,198),fill="green",start=self.frac(30),extent=self.frac(30))
        self.canvas1.create_text(60,95,text="Midterm--30%",tags="midterm")
        self.canvas1.create_arc((50,50,198,198),fill="orange",start=self.frac(60),extent=self.frac(40))
        self.canvas1.create_text(170,180,text="Final--40%",tags="final")
        
        window.mainloop()
        
    def frac(self,n):
        return 360*n/100
        
        
piechart()