sum=0
n=int(input("Enter an integer: "))
while(n!=0):
    d=n%10
    sum=sum+d
    n=n//10
print("Sum of digits is:",sum)
