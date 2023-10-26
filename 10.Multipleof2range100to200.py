for i in range(100,200):
    n=i
    sum=0
    while(n!=0):
        d=n%10
        sum=sum+d
        n=n//10
    if(sum%2==0):
        print(i)
