
file1 = input("Enter a filename: ").strip()
removal_str = input("Enter the string to be removed: ")
read_handle = open(file1, "r")
full_file = read_handle.read()
read_handle.close()

write_handle = open(file1,"w")
replaced_file = full_file.replace(removal_str,"")
write_handle.write(replaced_file)
write_handle.close

print("Done")