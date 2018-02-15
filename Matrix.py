#Matrix multipilcation

m1=[[],[],[],[],[]]
m,n=int(input("Enter the no.of Rows : ")),int(input("Enter the no.of Columns : "))
print("Enter the Elements into Matrix : ")
for i in range(m):
    for j in range(n):
        m1[i].append(int(input()))
print(m1)

m2=[[],[],[],[],[]]
print("Enter the no.of Rows & Columns  of 2nd Matrix: ")
p,q=int(input("Enter the no.of Rows : ")),int(input("Enter the no.of Columns : "))
print("Enter the Elements into Matrix : ")
for i in range(m):
    for j in range(n):
        m2[i].append(int(input()))
print(m2)

mm=[[],[],[],[],[]]
if(n==p):
    for i in range(m):
        for j in range(q):
            mm[i].append(0)
            for k in range(p):
                mm[i][j]+=m1[i][k]*m2[k][j]
    print("Multipilcation: ",mm)
else:
    print("Matrix Multiplication is Not Possible ")
