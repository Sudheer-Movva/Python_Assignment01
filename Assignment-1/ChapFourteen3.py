import keyword
file_name = input("Enter a Python source code file name: ")

read_handle = open(file_name,"r")
full_file = read_handle.read()
words_list = full_file.split()

count = 0
keyWords = {}
for each in words_list:
    if keyword.iskeyword(each):
        if each in keyWords:
            keyWords[each] += 1
        else:
            keyWords[each] = 1 


for each_key in keyWords:
    print(str(each_key) +" has " + str(keyWords[each_key]) + " occurrences")     