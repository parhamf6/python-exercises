n = int(input())
flist = [1,2]
tlist = [1,2]
for i in range(n):
    tvalue = tlist[i]+tlist[i-1]
    tlist.append(tvalue)
print(tlist)