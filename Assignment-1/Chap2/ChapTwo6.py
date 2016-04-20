#Chapter 2 - 6

input_int = eval(input("Enter any integer between 0 and 1000: "))

digit1 = input_int%10
print("First digit is: ", digit1)

rem_int1 = input_int//10
print("Remaining integer is: ", rem_int1)
    
digit2 = rem_int1%10
print("Second digit is: ", digit2)

rem_int2 = rem_int1//10
print("Remaining integer is: ", rem_int2)

digit3 = rem_int2%10
print("Third digit is: ", digit3)

rem_int3 = rem_int2//10
print("Remaining integer is: ", rem_int3)

sum_int_digits = digit1 + digit2 + digit3
print("Sum of all digits in a integer is: ",sum_int_digits)
