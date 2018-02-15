p=0
n=0
l=list()
t=int(input("Enter the total no.of numbers :"))
print("Enter the Numbers :")
for i in range(1,t+1):
      a=int(input())
      l.append(a)
for i in l:
      if i>0:
            p=p+i
      else:
           n=n+i
print("Sum of -ve values : ",n)
print("Sum of +ve values : ",p)
 
