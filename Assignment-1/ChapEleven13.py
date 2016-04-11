
def locateLargest(lst):
    largest_elem = lst[0][0]
    location_row = 0
    location_column = 0
    for row in range(len(lst)):
        for col in range(len(lst[0])):
            if lst[row][col] >= largest_elem:
                largest_elem = lst[row][col]
                location_row = row
                location_column = col  
    
    print("The location of the largest element is at (",location_row,",",location_column,")")

rows_num = eval(input("Enter the number of rows: "))
input_list = []
for i in range(rows_num):
    input_list.append([])
    items_list = input("Enter the columns for each row: ")
    items = items_list.split()
    for each in items:
        input_list[i].append(eval(each))


locateLargest(input_list)

    
    