
def reverse(number):
    rem = number
    reverse_number =""
    while rem!=0:
        reverse_number += str(rem%10)
        rem //= 10    
    return reverse_number
    
def isPalindrome(number):
    if str(number) == str(reverse(number)):
        print("Entered number is a palindrome")
    else:
        print("Entered number is not a palindrome")
        

number = eval(input("Enter a number: "))
isPalindrome(number)