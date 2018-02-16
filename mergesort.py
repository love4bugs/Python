l=list()
n=int(input("Enter The Number of Elements :"))
for _ in range(n):
    l.append(int(input("Enter the Number :")))
def merge(l,lo,mid,hi):
    a=l[lo:mid+1]
    b=l[mid+1:hi+1]
    a.append(10000000000)
    b.append(10000000000)
    p=q=0
    for i in range(lo,hi+1):
        if a[p]<=b[q]:
            l[i]=a[p]
            p+=1
        else:
            l[i]=b[q]
            q+=1
def mergesort(l,lo,hi):
    if lo<hi:
        mid=(lo+hi)//2
        mergesort(l,lo,mid)
        mergesort(l,mid+1,hi)
        merge(l,lo,mid,hi)
        print(l)

mergesort(l,0,n-1)
print("After Merge sort : ",l)
