def binarySearch(numbers,lower,upper,x):
    if (upper>=lower):
        mid=lower+(upper-lower)//2
        if (numbers[mid]==x):
            return mid
        elif (numbers[mid]>x):
            return binarySearch(numbers,lower,mid-1,x)
        else:
            return binarySearch(numbers,mid+1,upper,x)
    else:
        return -1
numbers = [1,4,6,7,12,17,25]
x=17
result = binarySearch(numbers,0,len(numbers)-1,x)
if (result!=-1):
    print("element found at position:",result)
else:
    print("The given element is not present in the array")

