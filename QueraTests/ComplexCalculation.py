import math
s = str(input())
slist = s.rsplit(" ")
x=int(slist[0])
a=int(slist[1])
n=int(slist[2])
a=0
nf=math.factorial(n)
for i in range(0,n+1):
    fp = (nf/(math.factorial(n-i)*math.factorial(i)))
    lp = (math.pow(x,i))*(math.pow(a,(n-i)))
    a=a+(fp*lp)
print(a)
