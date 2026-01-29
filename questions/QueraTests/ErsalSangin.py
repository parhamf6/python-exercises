# ارسال سنگین
# https://quera.org/problemset/3558
s = str(input()).split(" ")
n, m = int(s[0]), int(s[1])
nw = []
mw = []
for ni in range(n):
    ns = str(input()).split(" ")
    sr , er = int(ns[0]), int(ns[1])
    for i in range(sr,er+1):
        nw.append(i)
for ni in range(m):
    ms = str(input()).split(" ")
    sr , er = int(ms[0]), int(ms[1])
    for i in range(sr,er+1):
        mw.append(i)
count_same = 0
for c in nw:
    if c in mw:
        count_same+=1
print(count_same)