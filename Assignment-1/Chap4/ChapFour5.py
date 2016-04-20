
input_day = eval(input("Enter today\'s day: "))
elapsed_days = eval(input("Enter the elapsed days since today: "))
ip_week_day = "Input Week Day"
op_week_day = "Output Week Day"

if input_day == 0:
    ip_week_day = "Sunday"
elif input_day == 1:
    ip_week_day = "Monday"
elif input_day == 2:
    ip_week_day = "Tuesday"
elif input_day == 3:
    ip_week_day = "Wednesday"
elif input_day == 4:
    ip_week_day = "Thursday"
elif input_day == 5:
    ip_week_day = "Friday"
elif input_day == 6:
    ip_week_day = "Saturday"
else:
    print("Enter values between 0 and 6")

edays_rem = (input_day+elapsed_days)%7
#print("Elapsed day remaining: ",edays_rem)

if edays_rem == 0:
    op_week_day = "Sunday"
elif edays_rem == 1:
    op_week_day = "Monday"
elif edays_rem == 2:
    op_week_day = "Tuesday"
elif edays_rem == 3:
    op_week_day = "Wednesday"
elif edays_rem == 4:
    op_week_day = "Thursday"
elif edays_rem == 5:
    op_week_day = "Friday"
elif edays_rem == 6:
    op_week_day = "Saturday"
else:
    print("Some issue with calculation")


print("Today is ",ip_week_day, " and the future day is ",op_week_day)