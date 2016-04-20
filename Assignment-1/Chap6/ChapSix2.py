
def sumDigits(n):
    sum_digits = 0
    rem = n
    while rem !=0:
        sum_digits += rem%10
        rem //= 10
    print("Sum of the digits in ",n," is: ", sum_digits)
    
sumDigits(eval(input("Input a integer: ")))