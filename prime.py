n=int(input("Enter a value : "))
flag=0;
if n<2:
    flag=1
else:
    for i in range(2,n):
        if n%i==0:
            flag=2
            break
if flag==1:
    Print(n," is NOT PRIME")
else:
    Print(n," is PRIME")
