s = str(input())
slist=s.rsplit(" ")
n = float(slist[0])
k = float(slist[1])
p = float(slist[-1])
nk = n*k
pnk = nk * p
print(int(pnk))