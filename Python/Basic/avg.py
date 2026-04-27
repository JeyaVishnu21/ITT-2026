#To find average of three numbers 
a=int(input("Enter mark:"));
b=int(input("Enter mark:"));
c=int(input("Enter mark:"));
print("Total:",a+b+c,"Average:{0.2F}".Format((a+b+c)/3)) if( a>=0 and a<=100 and b>=0 and b<=100 and c>=0 and c<=100) else print("Invalid");
