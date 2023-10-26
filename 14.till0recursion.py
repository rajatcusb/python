def recursion1(n):
    if n>=0:
        print(n)
        recursion1(n-1)
n=int(input("Enter a number: "))
recursion1(n)
