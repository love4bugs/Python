l=list()
len=int(input("Enter the length of list :"))
print("Enter the list Numbers :")
for i in range(1,len+1):
    l.append(int(input()))
key=int(input("Enter the key : "))
for i in range(0,len):
    if key==l[i]:
        break
if l[i]==key:
    print(key," is found in ",i," position")
else:
    print(key," is NOT found")
