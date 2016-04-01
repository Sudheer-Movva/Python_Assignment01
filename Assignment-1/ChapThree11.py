
input_4digit_num = eval(input("Enter a four digit integer: "))

first_digit = input_4digit_num % 10
first_remaining = input_4digit_num // 10


second_digit = first_remaining % 10
second_remaining = first_remaining // 10


third_digit = second_remaining % 10
third_remaining = second_remaining // 10


fourth_digit = third_remaining % 10
fourth_remaining = third_remaining // 10

print("Entered integer " + str(input_4digit_num) + " in reverse order is: " +str(first_digit)+str(second_digit)+str(third_digit)+str(fourth_digit))