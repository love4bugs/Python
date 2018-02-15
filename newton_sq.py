n=float(input("Enter a value : "))
a=1
for _ in range(10):
    a=(a+n/a)/2
print("The sq.root of ",n," by Newton's Method is : ",a)
