
input_emp_name = input("Enter employee name: ")
input_hours_week = eval(input("Enter no.of hours worked in a week: "))
input_hour_rate =  eval(input("Enter hourly pay rate: "))
input_federal_tax =  eval(input("Enter federal tax withholding rate: "))
input_state_tax =  eval(input("Enter state tax withholding rate: "))

gross_pay = input_hours_week * input_hour_rate
federal_withholding = round(gross_pay * input_federal_tax,2)
state_withholding = round(gross_pay * input_state_tax,2)

net_pay = gross_pay - federal_withholding - state_withholding

print("Employee name: ",input_emp_name)
print("Hours worked: ",input_hours_week)
print("Pay rate: $",input_hour_rate)
print("Gross pay: $",gross_pay)
print("Deductions: ")
print("\tFederal withholding (",format(input_federal_tax,"6.1%"),"): $",federal_withholding)
print("\tState withholding (",format(input_state_tax,"6.1%"),"): $",state_withholding)
print("\tTotal deduction: $",federal_withholding+state_withholding)
print("Net pay: $",net_pay)