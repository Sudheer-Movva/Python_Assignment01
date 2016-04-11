import random

input_list = []
for row in range(4):
    input_list.append([])
    for col in range(4):
        input_list[row].append(random.randint(0,1))
print(input_list)
print()
        
for row in range(len(input_list)):
    for each in input_list[row]:
        print(each,end=" ")
    print()

row_score = []
row_count = 0
    
for row in range(len(input_list)):
    for col in range(len(input_list[row])):
        if input_list[row][col] == 1:
            row_count += 1
    row_score.append(row_count)
    row_count = 0
    
unsorted_row_score = [] + row_score
row_score.sort()

print("The largest row index: ",end="")
for item in range(len(unsorted_row_score)):
    if unsorted_row_score[item] == row_score[len(row_score)-1]:
        print(item,end=", ")

col_score = []
col_count = 0    
for col in range(len(input_list)):
    for row in range(len(input_list[col])):
        if input_list[row][col] == 1:
            col_count += 1
    col_score.append(col_count)
    col_count = 0
    
unsorted_col_score = [] + col_score
col_score.sort()

print()
print("The largest column index: ",end="")
for item in range(len(unsorted_col_score)):
    if unsorted_col_score[item] == col_score[len(col_score)-1]:
        print(item,end=", ")


