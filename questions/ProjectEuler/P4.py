# problem 4
l = []
for i in range(100,1000):
    for z in range(100,1000):
        r = i * z
        rs = str(r)
        rsr = rs[::-1]
        if rs == rsr:
            l.append(int(rs))
l.sort()
print(l[-1])
