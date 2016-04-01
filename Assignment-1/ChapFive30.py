
year,first_day =eval(input("Enter the year and the first day of the year: "))

if first_day%7 == 1:
    day_name = "Monday"
elif first_day%7 == 2:
    day_name = "Tuesday"
elif first_day%7 == 3:
    day_name = "Wednesday"
elif first_day%7 == 4:
    day_name = "Thursday"
elif first_day%7 == 5:
    day_name = "Friday"
elif first_day%7 == 6:
    day_name = "Saturday"
else:
    day_name = "Sunday"
        
print("January 1 ",year," is ",day_name)

days_sum = 1 + 32

for month in range(2,13):
    if month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if days_sum%7 == 1:
            day_name = "Monday"
        elif days_sum%7 == 2:
            day_name = "Tuesday"
        elif days_sum%7 == 3:
            day_name = "Wednesday"
        elif days_sum%7 == 4:
            day_name = "Thursday"
        elif days_sum%7 == 5:
            day_name = "Friday"
        elif days_sum%7 == 6:
            day_name = "Saturday"
        else:
            day_name = "Sunday"
            
        if month == 3:
            month_name = "March"
        elif month == 5:
            month_name = "May"
        elif month == 7:
            month_name = "July"
        elif month == 8:
            month_name = "August"
        elif month == 10:
            month_name = "October"
        elif month == 12:
            month_name = "December"
            
        days_sum += 31
    
    if month == 4 or month == 6 or month == 9 or month == 11:
        if days_sum%7 == 1:
            day_name = "Monday"
        elif days_sum%7 == 2:
            day_name = "Tuesday"
        elif days_sum%7 == 3:
            day_name = "Wednesday"
        elif days_sum%7 == 4:
            day_name = "Thursday"
        elif days_sum%7 == 5:
            day_name = "Friday"
        elif days_sum%7 == 6:
            day_name = "Saturday"
        else:
            day_name = "Sunday"
            
        if month == 4:
            month_name = "April"
        elif month == 6:
            month_name = "June"
        elif month == 9:
            month_name = "September"
        elif month == 11:
            month_name = "November"
            
        days_sum += 30
    
    if month == 2:
            
        if days_sum%7 == 1:
            day_name = "Monday"
        elif days_sum%7 == 2:
            day_name = "Tuesday"
        elif days_sum%7 == 3:
            day_name = "Wednesday"
        elif days_sum%7 == 4:
            day_name = "Thursday"
        elif days_sum%7 == 5:
            day_name = "Friday"
        elif days_sum%7 == 6:
            day_name = "Saturday"
        else:
            day_name = "Sunday"
        
        if month == 2:
            month_name = "Febraury"
        if year%4 == 0:
            days_sum += 29
        else:
            days_sum += 28
        
            
    print(month_name," 1 ",year," is ",day_name)
    