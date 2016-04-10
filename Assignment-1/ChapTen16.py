

def bubbleSort(lst):
    for i in range(len(lst),2):
        if lst[i] > lst[i+1]:
            temp = lst[i+1]
            lst[i+1] = lst[i]
            lst[i] = temp
    


input_list = input("Enter a list of 10 numbers: ")
input_items = input_list.split()
lst = [eval(x) for x in input_items]
