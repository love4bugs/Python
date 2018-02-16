str1=input("Enter 1st string : ");
str2=input("Enter 2nd string : ");
count1,count2=0,0
for i in str1:
    count1+=1
for i in str2:count2+=1
if count1>count2:
    print("Str1 is Greater Than str2")
elif count1==count2:
    print("Str1 is Equal To str2")
else:
    print("Str2 is Greater Than str1")
