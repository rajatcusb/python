n=[]
count=0
y=int(input("Enter how many elements you want:"))
for i in range(0,y):
        z=int(input())
        n.append(z)
for i in range(len(n)):
    if(n[i]%2!=0):
        count=count+1
print("The number of odd numbers in the list are: ", count)
