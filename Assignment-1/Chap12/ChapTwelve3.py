
class Account:
    def __init__(self,id,balance=100):
        self.__id = int(id)
        self.__balance = float(balance)
        
    def getID(self):
        return self.__id
    
    def getBalance(self):
        return self.__balance
    
    def withdraw(self,amount):
        self.__balance -= float(amount)
    
    def deposit(self,amount):
        self.__balance += float(amount)
    

account_list = []
for i in range(10):
    account = Account(i)
    account_list.append(account)
    #account_list.append(account.getID(),account.getInitialBalance())

while 1<2 :
    account_id = eval(input("Enter an Account ID: "))
    found = False
    selected_account=[]
    for idx in range(len(account_list)):
        if account_list[idx].getID() == account_id:
            found = True
            selected_account.append(account_list[idx])
            break
    #print(selected_account[0].getID())
    if not found:
        print("Enter a correct ID")
        continue
    if found:
        print("Main Menu")
        print("1: check balance")
        print("2: withdraw")
        print("3: deposit")
        print("4: exit")
    choice = eval(input("Enter a choice: "))
    
    if (choice == 1):
        print("The balance is ",selected_account[0].getBalance())
    elif (choice == 2):
        amount = eval(input("Enter an amount to withdraw:"))
        selected_account[0].withdraw(amount)
        print("The balance is ",selected_account[0].getBalance())
    elif (choice == 3):
        amount = eval(input("Enter an amount to deposit:"))
        selected_account[0].deposit(amount)
        print("The balance is ",selected_account[0].getBalance())
    elif (choice == 4):
        continue
    
    