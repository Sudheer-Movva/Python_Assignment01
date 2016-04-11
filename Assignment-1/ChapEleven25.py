
def isMarkovMatrix(lst):
    Markov = True
    for col in range(len(lst)):
        sum1 = 0
        for row in range(len(lst)):
            if lst[row][col] <= 0:
                Markov = False
                return Markov
            else:
                print(lst[row][col])
                sum1 += lst[row][col]
        if sum1 != 1:
            Markov = False
            return Markov
    return Markov
    
    

print("Enter a 3*3 matrix row by row: ")
row_1 = input("")
row_2 = input("")
row_3 = input("")
input_list = []

items1 = row_1.split()
if len(items1) > 0:
    input_list.append([])
for each in items1:
    input_list[0].append(eval(each))

items2 = row_2.split()
if len(items2) > 0:
    input_list.append([])
for each in items2:
    input_list[1].append(eval(each))
    
items3 = row_3.split()
if len(items3) > 0:
    input_list.append([])
for each in items3:
    input_list[2].append(eval(each))

print(input_list)


Markov = isMarkovMatrix(input_list)

if Markov:
    print("It is a Markov matrix")
    
if not Markov:
    print("It is not a Markov matrix")

