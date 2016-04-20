from tkinter import *
import math

class InvestmentCalculator:
    def __init__(self):
        window = Tk()
        window.title("Investment-Value Calculator")
        Label(window, text = "Investment Amount").grid(row = 1,column = 1, sticky = W)
        Label(window, text = "Years").grid(row = 2,column = 1, sticky = W)
        Label(window, text = "Annual Interest Rate").grid(row = 3,column = 1, sticky = W)
        Label(window, text = "Future Value").grid(row = 4,column = 1, sticky = W)
        
        self.investmentAmountVar = StringVar()
        Entry(window, textvariable = self.investmentAmountVar,justify = RIGHT).grid(row = 1, column = 2)
        self.yearsVar = StringVar()
        Entry(window, textvariable = self.yearsVar,justify = RIGHT).grid(row = 2, column = 2)
        self.annualInterestRateVar = StringVar()
        Entry(window, textvariable = self.annualInterestRateVar,justify = RIGHT).grid(row = 3, column = 2)
        self.futureValueVar = StringVar()
        Entry(window, textvariable = self.futureValueVar,justify = RIGHT).grid(row = 4, column = 2)
        
        buttonValue = Button(window,text="Calculate",command=self.computeInvestment).grid(row=5,column=2,sticky=E)
        window.mainloop()
        
    def computeInvestment(self):
        futureValueVar = (float(self.investmentAmountVar.get())) * math.pow((1 + (float(self.annualInterestRateVar.get())/12)),int(self.yearsVar.get())*12)
        self.futureValueVar.set(format(futureValueVar,"10.2f"))
     
InvestmentCalculator()       

