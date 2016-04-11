
input_list = input("Enter students\' names and scores: ")
items = input_list.split()

num_rows = len(items)//2
num_cols = 2
lst_2by2 = []

for row in range(num_rows):
    lst_2by2.append([])
    for col in range(1,-1,-1):
        lst_2by2[row].append(items.pop(col))
print("before sort: ",lst_2by2)

lst_2by2.sort()
print("after sort:",lst_2by2)

for row in range(len(lst_2by2)):
    for col in range(len(lst_2by2[row])-1,-1,-1):
        print(lst_2by2[row][col],end=" ")
    print()