# problem 56
s = []
for a in range(1,100):
    for b in range(1,100):
        s.append(a**b)
ss = []
for i in s:
    su = 0
    for c in str(i):
        su=su+int(c)
    ss.append(su)
ss.sort()
print(ss[-1])
