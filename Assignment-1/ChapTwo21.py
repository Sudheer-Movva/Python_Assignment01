input_savings_amount = eval(input("Enter the monthly savings amount: "))

monthly_int_rate = 0.05/12
print("Monthly interest rate: ",monthly_int_rate)

cons_multiple = 1 + monthly_int_rate

First_month_savings = input_savings_amount * cons_multiple
Second_month_savings = (input_savings_amount + First_month_savings) * cons_multiple
Third_month_savings = (input_savings_amount + Second_month_savings) * cons_multiple
Fourth_month_savings = (input_savings_amount + Third_month_savings) * cons_multiple
Fifth_month_savings = (input_savings_amount + Fourth_month_savings) * cons_multiple
Sixth_month_savings = (input_savings_amount + Fifth_month_savings) * cons_multiple

print("After the sixth month, the account value is: ",round(Sixth_month_savings,2))