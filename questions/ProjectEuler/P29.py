# problem 29
res = []
for a in range(2,101):
    for b in range(2,101):
        c = a**b
        if c not in res:
            res.append(c)
print(len(res))