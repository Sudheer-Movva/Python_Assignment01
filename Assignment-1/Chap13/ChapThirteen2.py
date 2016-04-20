
file_name = input("Enter a filename: ").strip()
read_handle = open(file_name, "r")
full_file = read_handle.read()

print(str(len(full_file)) + " characters") 
print(str(len(full_file.split())) + " words") 
print(str(len(full_file.split('\n'))) + " lines") 
    
read_handle.close()
