n = int(input())
tlist = []
flist = []
for i in range(n):
    x =  str(input())
    tlist.append(x)
for z in tlist:
    z = str(z).lower()
    z = str(z).title()
    flist.append(z)
for p in flist:
    print(p)