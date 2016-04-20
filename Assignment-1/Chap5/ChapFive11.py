
input_count = eval(input("Enter the number of students: "))
count = input_count
max1 = 0

while count != 0:
    count -= 1
    score = eval(input("Enter the student" + str(input_count-count) + " score: "))
    
    if score > max1:
        max2 = max1
        max1 = score
        #print("max1 is ",max1)
        
print("Highest and second-highest scores are: ", max1, " and ",max2)    