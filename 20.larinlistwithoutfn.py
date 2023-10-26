n=[3,8,1,7,2,9,5,12,4]
largest=n[0]
pos=0
for i in range(len(n)):
    if (n[i]>largest):
        largest=n[i]
        pos=i
print("The largest element is ",largest,)
