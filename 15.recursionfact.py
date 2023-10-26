def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
n=int(input("Enter a number: "))
if n<0:
    print("Enter valid numbers")
elif n==0:
    print("The factorial of 0 is 1")
else:
    result=factorial(n)
    print("factorial=",result)
