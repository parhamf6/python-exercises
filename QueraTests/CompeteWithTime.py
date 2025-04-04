k = int(input())
n = int(input())
h = str(input())
hlist = h.rsplit(" ")
tlist = [int(hlist[0])]
tot = (n*1)
o = 0
while o!=(int(n))-1:
    a = int(hlist[o])
    f = int(hlist[int(o)+1])
    x = a - f
    z = abs(x)
    tlist.append(z)
    o = o +1
tlist.append(int(hlist[-1]))

for b in tlist:
    q = int(b)
    q2 = q%k
    if q<k:
        tot = tot +1
    else:
        if q2==0:
            v = int(q/k)
            tot = tot + v
        if q2!=0:
            v = int(q/k)
            tot = tot + v + 1

print(tot)