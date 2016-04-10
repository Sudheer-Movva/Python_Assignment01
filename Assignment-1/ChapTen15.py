
def isSorted(lst):
    sorted = True
    for i in range(1,len(lst)):
        if lst[i-1] > lst[i]:
            sorted = False
            break
    if not sorted:
        print("The List is not sorted")
    else:
        print("The List is sorted")
            
input_list = input("Enter list: ")
input_items = input_list.split()
lst = [eval(x) for x in input_items]

isSorted(lst)
