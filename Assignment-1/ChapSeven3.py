
class Account:
    def __init__(self,id=0,balance=100,annualInterestRate=0):
        self.__id = id
        self.__balance = float(balance)
        self.__annualInterestRate = float(annualInterestRate)
    
    def setId(self,id):
        self.__id = id
    
    def setBalance(self,balance):
        self.__balance = balance
    
    def setannualInterestRate(self,annualInterestRate):
        self.__annualInterestRate = annualInterestRate
        
    def getId(self):
        return self.__id
    
    def getBalanace(self):
        return self.__balance
    
    def getannualInterestRate(self):
        return self.__annualInterestRate
    
    def getmonthlyInterestRate(self):
        return (self.__annualInterestRate / 12)
    
    def getmonthlyInterest(self):
        #return (self.__balance)*(self.__annualInterestRate / 12)*100
        return (self.getBalanace()*self.getmonthlyInterestRate())/100
    
    def withdraw(self,amount):
        self.__balance -= amount
        
    def deposit(self,amount):
        self.__balance += amount