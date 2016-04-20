
a,b,c,d,e,f = eval(input("Enter a,b,c,d,e,f: "))

denom = (a*d)-(b*c) 
if denom == 0:
    print("The equation has no solution")
else:
    x = ((e*d) - (b*f))/denom
    y = ((a*f) - (e*c))/denom
    print("x is ",x," and y is ",y)
    