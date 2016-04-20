def merge(list1, list2):
    merged_list = []
    current1 = 0
    current2 = 0
    
    while current1 < len(list1) and current2 < len(list2):
        if list1[current1] < list2[current2]:
            merged_list.append(list1[current1])
            current1 += 1
        else:
            merged_list.append(list2[current2])
            current2 += 1
            
    while current1 < len(list1):
        merged_list.append(list1[current1])
        current1 += 1

    while current2 < len(list2):
        merged_list.append(list2[current2])
        current2 += 1

    return merged_list

s1 = input("Enter list1: ") 
items = s1.split()
list1 = [ eval(x) for x in items ]

s2 = input("Enter list2: ") 
items = s2.split()
list2 = [ eval(x) for x in items ]
    
list3 = merge(list1, list2);
    
print("The merged list is ", list3)