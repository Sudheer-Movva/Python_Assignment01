
def prefix(s1,s2):
    count = 0
    prefix_str = ""
    end = min(len(s1),len(s2))
    
    for i in range(0,end):
        if s1[i] == s2[i]:
            count += 1
            prefix_str += s1[i]
        else:
            break
    if count > 0:
        return prefix_str
    
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
print("Common prefix for ",str1," and ",str2," is ",prefix(str1,str2))