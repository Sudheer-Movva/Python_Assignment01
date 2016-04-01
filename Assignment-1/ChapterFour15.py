import random

input_number = eval(input("Enter a three-digit number: "))
random_number = random.randint(0,999)
print("The generated random number is: ",random_number)

#Getting the individual digits of the entered number
inputnum_digit1 = input_number%10
if input_number//10 !=0:
    inputnum_rem = input_number//10
inputnum_digit2 = inputnum_rem%10
if inputnum_rem//10 !=0:
    inputnum_rem = inputnum_rem//10
inputnum_digit3 = inputnum_rem%10

#Getting the individual digits of the random number
randomnum_digit1 = random_number%10
if random_number//10 !=0:
    randomnum_rem = random_number//10
randomnum_digit2 = randomnum_rem%10
if randomnum_rem//10 !=0:
    randomnum_rem = randomnum_rem//10
randomnum_digit3 = randomnum_rem%10

'''
print("Checking")
print("Input digits are: ",inputnum_digit1,":",inputnum_digit2,":",inputnum_digit3)
print("Random digits are: ",randomnum_digit1,":",randomnum_digit2,":",randomnum_digit3)
'''

if (input_number == random_number):
    print("You won $10,000 lottery amount")

if (inputnum_digit1 == randomnum_digit1 or inputnum_digit1 == randomnum_digit2 or inputnum_digit1 == randomnum_digit3):
    if (inputnum_digit2 == randomnum_digit1 or inputnum_digit2 == randomnum_digit2 or inputnum_digit2 == randomnum_digit3):
        if (inputnum_digit3 == randomnum_digit1 or inputnum_digit3 == randomnum_digit2 or inputnum_digit3 == randomnum_digit3):
            print("You won $3000 lottery amount")

elif ((inputnum_digit1 == randomnum_digit1 or inputnum_digit1 == randomnum_digit2 or inputnum_digit1 == randomnum_digit3) or
    (inputnum_digit2 == randomnum_digit1 or inputnum_digit2 == randomnum_digit2 or inputnum_digit2 == randomnum_digit3) or
        (inputnum_digit3 == randomnum_digit1 or inputnum_digit3 == randomnum_digit2 or inputnum_digit3 == randomnum_digit3)):
            print("You won $1000 lottery amount")
else:
    print("You didn't won any lottery")