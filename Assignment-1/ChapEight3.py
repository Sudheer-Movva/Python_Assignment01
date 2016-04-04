
password_str = input("Enter the password: ")
isValid = True
count = 0

if len(password_str) < 8:
    isValid = False
    
if not password_str.isalnum():
    isValid = False
    
for ch in password_str:
    if ch.isdigit():
        count += 1
if count < 2:
    isValid = False
    
if isValid:
    print("Entered password is Valid")
else:
    print("Entered password is invalid")
    