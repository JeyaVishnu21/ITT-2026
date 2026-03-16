#This program will judge the guess , if the number is guesed in the correct position add hit count if it is guessed in the wrong position add not hit count
#Display the number of hits and not hits
a=input("Enter a random number:")
b=input("Guess the number:")
h,n=0,0
x=list(a)
y=list(b)
for i in range (len(x)):
   if x[i]==y[i]:
      h+=1
   if y[i] in x:
      n+=1
n=n-h
print(h,'H',n,'N')
