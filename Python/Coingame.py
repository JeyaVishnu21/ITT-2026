#Suresh and Sundar plays  a game that who has more number of coin wins 
#Raja came in and give his coins to the losser and the they played the another supporter suresh came in and give his coins to the loser 
#Print N if Suresh wins in the end or Print S if sunder wins in the end 
a=int(input("Enter Suresh coin count:"))
b=int(input("Enter Sunder coin count:"))
c=int(input("Enter Raja coin count:")) 
d=int(input("ENTER sURESH coin count:"))
if a<b:
   a=a+c
else:
   b=b+c
if a<b:
   a=a+d
else:
   b=b+d
print ("N") if (a>b or a==b) else print("S")
