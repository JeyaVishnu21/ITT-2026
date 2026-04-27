#To find the gross salary of the employee

sal=int(input("Enter salary:"));
h=sal*0.2;
d=sal*0.1;
print("Gross Salary:",sal+h+d) if (sal>=5000 and sal<=50000) else print("INVALID");
