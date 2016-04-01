import random

def printMatrix(number):
    for i in range(0,number):
        for j in range(0,number):
            matrix_number = random.randint(0,1)
            print(format(matrix_number,"3d"), end="")
        print("")
        
printMatrix(number = eval(input("Enter a number to the display matrix of 0s and 1s: ")))