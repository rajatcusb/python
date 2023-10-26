def Fibonnaci(num):
    if num<0:
        print("The input is incorrect.")
    elif num==1:
        return 0
    elif num==2:
        return 1
    else:
        return Fibonnaci(num-1)+Fibonnaci(num-2)
print(Fibonnaci(10))
