n = int(input())
n2 = str(input())
tlist = n2.rsplit(" ")
zlist = []
tlist.sort()
print(tlist)
for a in range(n):
    if len(tlist)>=2:
        j = tlist[-1]
        tlist.pop(-1)
        zlist.append(j)
        m = tlist[0]
        zlist.append(m)
        tlist.pop(0)
    else:
        for a in tlist:
            zlist.append(a)
            tlist = []

tem = ""
for q in zlist:
    tem = f"{tem}{q} "
print((tem))