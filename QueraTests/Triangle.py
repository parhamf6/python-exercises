x= str(input())
alist=x.rsplit(" ")
a = int(alist[0])
b = int(alist[1])
c = int(alist[2])
if a + b > c and a + c>b and b+c>a and a+b+c==180 and a>0 and b>0 and c>0 and a<360 and b<360 and c <360:
    print("Yes")
else:
    print("No")