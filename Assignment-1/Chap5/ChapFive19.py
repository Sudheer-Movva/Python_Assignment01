
input_lines = eval(input("Enter the number of lines: "))

for line in range(1,input_lines+1):
    for space in range(0,input_lines-line):
        print(" ",end=" ")
    for decrement in range(line,0,-1):
        print(decrement,end=" ")
    for increment in range(2,line+1):
        print(increment,end=" ")
    print("")
    
    
