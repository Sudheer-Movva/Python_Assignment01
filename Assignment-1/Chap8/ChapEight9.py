import math

def binaryToHex(binary_value):
    binary_str = str(binary_value)
    decimal_value = 0
    count = len(binary_str) - 1 
    
    for digit in binary_str:
        decimal_value += (int(digit) * math.pow(2,count))
        count -= 1
    
    add_str1 = str("")
    hex_str = str("")
    
    while decimal_value !=0:
        remainder = str(int(decimal_value%16))
        decimal_value = int(decimal_value // 16)
        if remainder == "10":
            add_str1 = "A"
            print("here")
        elif remainder == "11":
            add_str1 = "B"
        elif remainder == "12":
            add_str1 = "C"
        elif remainder == "13":
            add_str1 = "D"
        elif remainder == "14":
            add_str1 = "E"
        elif remainder == "15":
            add_str1 = "F"
        else:
            add_str1 = remainder
        hex_str = add_str1 + hex_str
    print("The corresponding hexadecimal value is: ", hex_str)
    
binaryToHex(eval(input("Enter a binary value: ")))
