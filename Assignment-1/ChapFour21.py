
input_year = eval(input("Enter the year: (e.g. 2008): "))
input_month = eval(input("Enter the month: 1-12: "))
input_day = eval(input("Enter the day of the month: 1-31: "))

if input_month == 1 or input_month == 2:
    input_month = input_month+12
    input_year = input_year-1

year_century = input_year%100
century = input_year//100

day_week = (input_day + (26*(input_month+1)//10) + year_century + (year_century//4) + (century//4) + (5*century)) % 7

if day_week == 0:
    print("Day of the week is Saturday")
elif day_week == 1:
    print("Day of the week is Sunday")
elif day_week == 2:
    print("Day of the week is Monday")
elif day_week == 3:
    print("Day of the week is Tuesday")
elif day_week == 4:
    print("Day of the week is Wednesday")
elif day_week == 5:
    print("Day of the week is Thursday")
elif day_week == 6:
    print("Day of the week is Friday")
else:
    print("Some issue with the algorithm")