#This program will help you to find the length of the array after removing all the occurence of a elemnt
a=int(input("Enter length:"))
arr=[]
for i in range(0,a):
   f=int(input("enter array element:"))
   arr.append(f)
val=int(input("Enter value to remove:"))
j=0
for i in range (0,a):
   if arr[i]==val:
      j+=1
x=len(arr)
y=x-j
print("The length of array afer removing the given values is:",y)
