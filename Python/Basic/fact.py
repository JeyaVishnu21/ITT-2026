#To find factorial of a number
a=int(input("Enter a number:"))
b=a
res =1
while a!=0:
   res*=a
   a-=1
print("The Factorial of ",b,"is",res)
