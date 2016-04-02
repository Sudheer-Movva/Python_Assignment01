import ChapSeven3

my_account = ChapSeven3.Account(1122,20000,4.5)
my_account.withdraw(2500)
my_account.deposit(3000)

print("Account\'s Id: ",my_account.getId(),",balance: ",my_account.getBalanace(),\
      " monthly interest rate: ",my_account.getmonthlyInterestRate(),\
      " monthly interest amount: ",my_account.getmonthlyInterest())