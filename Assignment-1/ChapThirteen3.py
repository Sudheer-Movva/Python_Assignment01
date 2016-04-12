

file1 = input("Enter a filename: ").strip()

read_handle = open(file1, "r")
full_file = read_handle.read()
read_handle.close()

scores_list = full_file.split()
print("There are ",len(scores_list)," scores")
total = 0
for each in scores_list:
    total += eval(each)

print("The total is ",total)
print("The average is ", round(total/len(scores_list),3))
    
    
