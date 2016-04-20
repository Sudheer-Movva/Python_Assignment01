import ChapSeven7

a,b,c,d,e,f = eval(input("Enter the values for a,b,c,d,e and f: "))

my_linear_equations = ChapSeven7.LinearEquation(a,b,c,d,e,f)

print("First 2*2 linear equation is: ",my_linear_equations.getA(),"X+",my_linear_equations.getB(),"Y=",my_linear_equations.getE())
print("Second 2*2 linear equation is: ",my_linear_equations.getC(),"X+",my_linear_equations.getD(),"Y=",my_linear_equations.getF())

if not my_linear_equations.isSolvable():
    print("The equations have no solution")
else:
    print("Solution for these linear equations are: ",my_linear_equations.getX()," and ",my_linear_equations.getY())