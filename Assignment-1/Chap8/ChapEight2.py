
str1 = input("Enter the first string: ").strip()
str2 = input("Enter the second string: ").strip()

def isASubstring(s1, s2):
    index_start = 0
    rem_len = len(s2)
    while len(s1) <= rem_len:
        if s1!= s2[index_start : index_start + len(s1)]:
            index_start += 1
            rem_len += 1
        else:
            return index_start
    return -1

if isASubstring(str1,str2) != -1:
    print("First string is a substring of the second string")
else:
    print("First string is not a substring of the second string")