import math

input_list = input("Enter numbers separated by spaces in one line: ")
input_items = input_list.split()
numbers = [eval(x) for x in input_items]

mean = sum(numbers)/len(numbers)

sum =0

for each in numbers:
    sum += math.pow((each-mean),2)

deviation = (sum/(len(numbers)-1))**0.5

print("mean of numbers: ",round(mean,2))
print("standard deviation of numbers: ",round(deviation,5))
