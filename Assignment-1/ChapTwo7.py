#Chapter 2 - 7

input_mins = eval(input("Enter the number of minutes: "))

tot_days = input_mins//(24*60)
years = tot_days//365
days = tot_days%365

print(input_mins," is approximately ",years," years and ",days," days")