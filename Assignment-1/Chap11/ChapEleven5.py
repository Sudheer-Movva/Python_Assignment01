
def addMatrix(lst1,lst2):
    result_list = []
    for i in range(len(lst1)):
        result_list.append([])
        for j in range(len(lst1[i])):
            result_list[i].append(lst1[i][j] + lst2[i][j])
            
    return result_list


list1_nbyn = []
for i in range(3):
    list1_nbyn.append([])
    list_row = input("Enter a 3*3 matrix row for row " + str(i+1) + ":")
    items = list_row.split()
    for each in items:
        list1_nbyn[i].append(eval(each))
'''        
items = list_row.split() = []
row = 0
col = 0
matrix = len(items)//3
list_row = input("Enter a 3*3 matrix row for row " + str(i+1) + ":")
items = list_row.split()
for each in items:
    
    
         
    list1_nbyn.append([])
    list_row = input("Enter a 3*3 matrix row for row " + str(i+1) + ":")
    items = list_row.split()
    for each in items:
        list1_nbyn[i].append(eval(each))
'''

list2_nbyn = []
for i in range(3):
    list2_nbyn.append([])
    list_row = input("Enter a 3*3 matrix row for row " + str(i+1) + ":")
    items = list_row.split()
    for each in items:
        list2_nbyn[i].append(eval(each))


print(list1_nbyn)
print(list2_nbyn) 

print("The matrices are added as follows: ")

for row in range(len(list1_nbyn)):
    for each in list1_nbyn[row]:
        print(each,end=" ")
    print()

print(" + ")

for row in range(len(list2_nbyn)):
    for each in list2_nbyn[row]:
        print(each,end=" ")
    print()


print_list = addMatrix(list1_nbyn,list2_nbyn)
print(" = ")
for row in range(len(print_list)):
    for each in print_list[row]:
        print(each,end=" ")
    print()
