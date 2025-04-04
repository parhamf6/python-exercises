k = int(input())
s = str(input())
rlist = []
res = 0
for i in range(k):
    num = str(input())
    numrev = num[::-1]
    tn = 0
    tnr = 0
    for n in num:
        if n!=s[int(i)]:
            tn = tn +1
    for nr in numrev:
        if nr!=s[int(i)]:
            tnr = tnr +1
    if tn > tnr:
        rlist.append(tnr)
    if tnr>tn:
        rlist.append(tn)
for r in rlist:
    res = res + int(r)
print(rlist)
print(res)