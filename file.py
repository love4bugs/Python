file = open("a.txt",'a')
line = input("Enter a sting to store : ")
file.write(line)
file.close()
fh=open("a.txt",'r')
for line in fh:
    print(line,'\n')
fh.close()
