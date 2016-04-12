
def sumDigits(n):
    digit = n%10
    rem = n//10
    if n != 0:
        return digit + sumDigits(rem)
    else:
        return 0
        
    
input_int = eval(input("Enter an integer: "))
print("The sum of digits in ",input_int," is ",sumDigits(input_int))    