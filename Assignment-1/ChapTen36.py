from tkinter import *
import random

class LinearSearch:
    def __init__(self):
        window1 = Tk()
        window1.title("Linear Search")
        self.canvas1 = Canvas(window1, width=200,height=100,bg="white")
        self.canvas1.pack()        
        
        list1 = self.createRandom()
        x1 = 30
        y1 = 50
        x2 = 0
        y2 = 0
        bar = 10
        for each in list1:
            x2 = x1-each
            y2 = y1-each
            self.canvas1.create_rectangle(x1, y1, x2, y2, outline='black',tags="rect"+str(each))
            x1 = x1+bar
            y1 = y1+bar
        
        window1.mainloop()
        
    def createRandom(self):
        random_list = []
        for i in range(1,20):
            random_list.append(random.randint(1,20))
        print(random_list)
        return random_list
        
LinearSearch()
