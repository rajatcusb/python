x=[]
y=int(input("Enter how many elements you want:"))
for i in range(0,y):
        z=int(input())
        x.append(z)
result=1
for n in x:
    result=result*n   
gm=pow(result,1/y)
print("Geometric mean is:",gm)
