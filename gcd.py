n=int(input("Enter 1st value : "))
n1=int(input("Enter 2nd value : "))
for i in range(1,n+1):
    if n1%i==0 and n%i==0 :
        gcd=i
print("Gcd of ",n," and ",n1," is : ",gcd)
