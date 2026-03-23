#Get number of tyre and tell is manufacturing of bike is possible after manufacturing car with given tyre 

a= int(input("Enter number of tiers you have:"))
if a==0:
  print ("Without tyre nothing can be manufactured")
elif a%4==0 :
   print ("NO Bike manufacture");
elif a%4==2:
   print("YEs you can manufacture a bike")
else:
   print("No bike manufacture")
