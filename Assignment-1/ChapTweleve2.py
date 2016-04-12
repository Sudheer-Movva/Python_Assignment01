
class Location:
    def __init__(self,row,column,maximal):
        self.__row__ = int(row)
        self.__column__ = int(column)
        self.__maximal__ = float(maximal)
    
    def getRow(self):
        return self.__row__
    
    def getColumn(self):
        return self.__column__
    
    def getMaximal(self):
        return self.__maximal__
        

def locateLargest(lst):
    maximal = lst[0][0]
    max_row = 0
    max_column = 0
    for row in range(len(lst)):
        for col in range(len(lst[0])):
            if lst[row][col] >= maximal:
                maximal = lst[row][col]
                max_row = row 
                max_column = col
    return Location(max_row,max_column,maximal)

input_list = []    
num_rows,num_cols = eval(input("Enter the number of rows and columns in a list: "))
for i in range(num_rows):
    list1 = input("Enter Row: ")
    input_list.append([])
    for each in (list1.split()):
        input_list[i].append(eval(each))

l1 = locateLargest(input_list)
print("The location of the largest element is ",l1.getMaximal()," at (",l1.getRow(),",",l1.getColumn(),")")