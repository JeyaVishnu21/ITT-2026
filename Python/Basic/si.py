#To find the Simple Intrest 

a=int(input("Enter principle amount:"));
b=int(input("enter Rate of intrest:"));
c=int(input("Enter Time period:"));
print("Simple Intrest:",(a*b*c)/100) if ( a>=1 and a<=100000 and b>=1 and b<=20 and c>=1 and c<=10) else print("INVALID");
