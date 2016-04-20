
def sumMajorDiagnal(lst):
    sum1 = 0
    for idx in range(len(lst)):
        sum1 += lst[idx][idx]
    return sum1


list_nbyn = []
for i in range(4):
    list_nbyn.append([])
    list_row = input("Enter a 4*4 matrix row for row " + str(i+1) + ":")
    items = list_row.split()
    for each in items:
        list_nbyn[i].append(eval(each))
        
print(list_nbyn) 

print("Sum of the Major diagnal is: ",sumMajorDiagnal(list_nbyn))
