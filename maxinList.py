l=list()
len=int(input("Enter the total no.of numbers :"))
print("Enter the Numbers :")
for i in range(1,len+1):
    l.append(int(input()))
max=l[0]
for i in l:
    if max<i:
        max=i
    
print("Max of the list : ",max)    
