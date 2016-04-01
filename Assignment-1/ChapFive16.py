
n1,n2 = eval(input("Enter two integers to find their GCD: "))

gcd_found = False

if n1 > n2:
    d = n2
else:
    d = n1

while d > 1:
    if n1%d == 0 and n2%d == 0:
        gcd_found = True
        print("The GCD of ",n1," and ",n2," is ",d)
        break
    d -= 1
    
if not gcd_found:
    print("The GCD of ",n1," and ",n2," is 1")    
