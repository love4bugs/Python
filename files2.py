'''s=open*('a.txt','r').read()
word s=s.split()
d={}
for w in word:
    if w in d:
        d[w]+=1
    else:
        d[w]=1
    occurance=1
    largekey=' '
for key.val in d.item():
    if val>c:
        c=val
        large=key
print(large," is the most frequenty ")

'''

from collections import Counter

with open('a.txt') as fin:
    counter = Counter(fin.read().strip().split())

print(counter.most_common())
