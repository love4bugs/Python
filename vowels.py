str1=input("Enter a string : ")
v=c=0
for i in str1:
    if(i=='a' or i=='A' or i=='e' or i=='E' or i=='i' or i=='I' or i=='o' or i=='O' or i=='u' or i=='U'):
        v+=1
    else:
        c+=1
print("No.of vowels in ",str1," is ",v)
print("No.of consonents in ",str1," is ",c)
