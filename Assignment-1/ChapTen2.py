
number_elements = eval(input("Enter the number of elements: "))
numbers = []

for count in range(number_elements):
    number = eval(input("Enter a number: "))
    numbers.append(number)

rev_numbers = []    

for count in range(len(numbers),0,-1):
    rev_numbers.append(numbers[count-1])

print("Entered Elements: ",numbers)    
print("Elements in reverse order: ",rev_numbers)