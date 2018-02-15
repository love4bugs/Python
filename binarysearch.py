def bi(lo,hi):
    mid=lo+(hi-lo)//2
    if lo!=hi:
        if l[mid]==key:
             print(key," is Found")
             return 1
        elif(l[mid]>key):
             bi(lo,mid-1)
        elif(l[mid]<key):
             bi(mid+1,hi)

l=list()
len=int(input("Enter the length of list :"))
print("Enter the list Numbers :")
for i in range(1,len+1):
    l.append(int(input()))
key=int(input("Enter the key : "))
l.sort()
found=0
found=bi(0,len-1)
if found!=1:
    print(key," is Not Found")
