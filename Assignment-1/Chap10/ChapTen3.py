
input_list = input("Enter numbers separated by spaces in one line: ")
input_items = input_list.split()
numbers = [eval(x) for x in input_items]
numbers.sort()

distinct_numbers = []
for each in numbers:
        if each not in distinct_numbers:
            distinct_numbers.append(each)


for each_distinct in distinct_numbers:
    print(each_distinct," occurs ", numbers.count(each_distinct),end="")
    if numbers.count(each_distinct) > 1:
        print(" times")
    else:
        print(" time")
    
