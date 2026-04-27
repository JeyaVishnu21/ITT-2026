#To covert Celsius into Farhenheit without built-in functions

a=float(input("Enter Temperature in celsius:"));
print("Temperature in Fahrenheit:",(a*(9/5)+32))   if (a>=-50  and  a<=100) else print("INVALID");
