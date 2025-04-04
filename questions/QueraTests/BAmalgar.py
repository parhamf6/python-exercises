s = str(input())
slist = s.rsplit("?")
a = int(slist[0])
b = int(slist[1])
c = int(slist[2])
res = [(a*b*c),(a*(b+c)),((a+b)*c),(a+b+c)]
maxres = res[0]
for i in res:
    if maxres<i:
        maxres = i
print(maxres)
