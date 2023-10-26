import math
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
if (a!=0.0):
    d=(b*b)-(4*a*c) 
    if (d==0.0):
        print("The roots are real and equal.") 
        r=-b/(2*a)
        print("The roots are ", r,"and", r)
    elif(d>0.0):
        print("The roots are real and distinct.")
        r1 = (-b+(math.sqrt(d)))/(2*a) 
        r2 = (-b-(math.sqrt(d)))/(2*a)
        print("The root1 is: ", r1)
        print("The root2 is: ", r2)
    else:
        print("The roots are imaginary.")
        real=-b/(2*a)
        imag= math.sqrt(-d)/(2*a)
        print("The root1 is: ", real, "+ i",imag)
        print("The root2 is: ", real, "- i",imag)
else:
    print("Not a quadratic equation.")
