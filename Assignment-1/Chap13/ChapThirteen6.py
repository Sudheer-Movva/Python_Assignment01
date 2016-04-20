import urllib.request

input_file = urllib.request.urlopen("http://cs.armstrong.edu/liang/data/Lincoln.txt")
full_file = input_file.read()

print("The number of words in the file is " + str(len(full_file.split())))
