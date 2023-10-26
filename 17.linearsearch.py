def linearsearch(array,x):
   for i in range(len(array)):
      if array[i]==x:
         return i
   return -1
array=['t','u','t','o','r','i','a','l']
x='r'
print("element found at index "+str(linearsearch(array,x)))
