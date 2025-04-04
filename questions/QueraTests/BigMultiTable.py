n = int(input())
for i in range(1,n+1):
    res = []
    for x in range(1,n+1):
        r = i * x
        res.append(str(r))
        if x==n:
            print(" ".join(res))
