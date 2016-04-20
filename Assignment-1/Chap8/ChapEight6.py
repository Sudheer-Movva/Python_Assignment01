
def countLetters():
    input_str = input("Enter a string: ")
    count = 0
    for ch in input_str:
        if not ch.isspace() and ch.isalpha():
            count += 1
    
    print("Number of letters in the string is: ",count)

countLetters()