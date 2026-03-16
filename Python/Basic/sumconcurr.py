#To check if the sum of concurrent elements is 19 or not 
a=[1,7,2,5,12]
for i,j in range(0,4):
      if((a[i]+a[j])==19):
         print(a[i],a[j])
