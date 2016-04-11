'''
def merge(lst1,lst2):
    merged_sorted_list = []
    lst_1 = lst1
    lst_2 = lst2
    while (lst_1 and lst_2):
        if (lst_1[0] <= lst_2[0]): 
            item = lst_1.pop(0)
            merged_sorted_list.append(item)
        else:
            item = lst_2.pop(0)
            merged_sorted_list.append(item)
    
    if lst_1:
        merged_sorted_list.extend(lst_1)
    elif lst_2:
        merged_sorted_list.extend(lst_2)
    print("Merged & sorted list is: ", merged_sorted_list)
    
input_lst1 = input("Enter first list of numbers in ascending order with spaces: ")
items1 = input_lst1.split()
lst1 = (eval(x) for x in items1)

input_lst2 = input("Enter second list of numbers in ascending order with spaces: ")
items2 = input_lst2.split()
lst2 = (eval(x) for x in items2)

merge(lst1,lst2)
'''
def merge_sorted_lists(lst1, lst2, sorted_list = None):
    if sorted_list == None:
        sorted_list = []

    slice_index = 0
    for element in lst1:
        if element <= lst2[0]:
            sorted_list.append(element)
            slice_index += 1
        else:
            return merge_sorted_lists(lst2, lst1[slice_index:], sorted_list)

    return sorted_list + lst2

input_lst1 = input("Enter first list of numbers in ascending order with spaces: ")
items1 = input_lst1.split()
lst_1 = (eval(x) for x in items1)

input_lst2 = input("Enter second list of numbers in ascending order with spaces: ")
items2 = input_lst2.split()
lst_2 = (eval(x) for x in items2)

print(merge_sorted_lists(lst_1,lst_2))