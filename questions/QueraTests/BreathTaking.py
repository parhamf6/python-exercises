n = int(input())
a = str(input())
b = str(input())
alist = a.rsplit(" ")
blist = b.rsplit(" ")
t = 0
for i in range(n):
    x = int(alist[i])*int(blist[i])
    t = t + x
print(t)