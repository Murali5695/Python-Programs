# """ ax2+bx+c=0
    

# """
# import cmath
# a=float(input("Enter the number:"))
# b=float(input("Enter the number:"))
# c=float(input("Enter the number:"))
# d=b**2-(4*a*c)
# sol1=(-b+cmath.sqrt(d))/(2*a)
# sol2=(-b-cmath.sqrt(d))/(2*a)
# print(f"{sol1}and{sol2}")

import cmath 
def findRoots(a,b,c):
    d=(b**2)-(4*a*c)

    if d>0:
        print("roots are real and distint.")
        sol1=(-b+cmath.sqrt(d))/(2*a)
        sol2=(-b-cmath.sqrt(d))/(2*a)
        print(f"{sol1}and{sol2}")
    elif d==0:
        print("real and equal")
        sol1=(-b)/(2*a)
        print(f"{sol1}")
    else:
        print("complex roots")
        sol1=(-b+cmath.sqrt(d))/(2*a)
        sol2=(-b-cmath.sqrt(d))/(2*a)
        print(f"{sol1}and{sol2}")
a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
if a==0:
    print("Error")
else:
    findRoots(a,b,c)