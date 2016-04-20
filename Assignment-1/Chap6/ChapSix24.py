
def isPrime(number):
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            return False
        divisor += 1
    
    return True

def reverse(number):
    rem = number
    reverse_number =""
    while rem!=0:
        reverse_number += str(rem%10)
        rem //= 10    
    return reverse_number
    
def isPalindrome(number):
    if str(number) == str(reverse(number)):
        return True
    else:
        return False

palindromic_prime_count = 0
number = 2

while palindromic_prime_count <=100:
    if isPrime(number) and isPalindrome(number):
        palindromic_prime_count += 1
        print(format(number,"10d"), end=" ")
        if palindromic_prime_count%10 == 0:
            print("")
        
    number +=1