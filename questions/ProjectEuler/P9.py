# problem 9

res = []
for a in range(1,1000):
    for b in range(1,1000):
        c = 1000 -a -b
        if a < b < c :
            if (a**2)+(b**2)==(c**2):
                print(f"a={a}, b={b}, c={c}")
                print(f"Product: {a*b*c}")
                res.append(a*b*c)
print(res)
