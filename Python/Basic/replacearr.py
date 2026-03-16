#To replace all occurrence  of a element in an array
def rep(a,b,c):
   temp=a[c]
   a[c]=a[b]
   a[b]=temp
a=[1,2,3,4,3,1,3,5,7]
j=8
val=3
for i in range(0,len(a)):
   if a[i]==val:
      rep(a,a[i],a[j])
      j-=1
print(a)
