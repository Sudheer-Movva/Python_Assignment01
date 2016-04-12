
file_name = input("Enter a text file name: ")

read_handle = open(file_name,"r")
full_file = read_handle.read()

vowel_set = set(["A","E","I","O","U","a","e","i","o","u"])

count_vowels = 0
count_consonants = 0

for each in full_file:
    if each.isalpha():
        if each in vowel_set:
            count_vowels += 1
        else:
            count_consonants += 1

print("The number of vowels: ",count_vowels)
print("The number of consonants: ",count_consonants)