

def bubbleSort(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-1,i,-1):
            if lst[i] > lst[j]:
                temp = lst[j]
                lst[j] = lst[i]
                lst[i] = temp
    print(lst)


input_list = input("Enter a list of 10 numbers: ")
input_items = input_list.split()
lst = [eval(x) for x in input_items]

bubbleSort(lst)