n=int(input("Enter a number : "))
a=n
s=0
while n!=0:
    rem=n%10
    s+=rem
    n=n//10
print("The sum of digits of ",a," is : ",s)
