a = str(input())
alist =  a.rsplit(" ")
n = int(alist[0])
k = int(alist[-1])
x = 1+k
t = 1
if n==k:
    print(1)
else: 
    while x!=1:
        x = x + k
        t = t + 1
        if x>n:
            x=x - n
        if x==1:
            break
    print(t)
