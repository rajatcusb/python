n=int(input("Enter a number:"))
p=1
for i in range(2,n//2):
    if (n%i==0):
        p=0
        break
if(p==1):
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")
