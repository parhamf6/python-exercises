y = str(input())
tlist = y.rsplit(" ")
n = int(tlist[0])
k = int(tlist[-1])
f = str(input())
flist=f.rsplit(" ")
temp = []
for i in flist:
    x = int(i) + 1
    temp.append(x)
temp.sort()
sum = 0
t = 0
for i in temp:
    if sum<k:
        sum = sum + int(i)
        t = t+1
        if sum>=k:
            sum = sum - int(i)
            t = t-1
            print(t)
    else:
        print(t)