t = int(input())
reslist = []
for i in range(t):
    n = int(input())
    nstr = str(input())
    q = 0
    c = 0
    for s in nstr:
        if q!=25 or c!=25:
            if s=="Q":
                q = q+1
            if s=="C":
                c = c+1
        if q==25 or c==25:
            if q==25:
                reslist.append("Quera")
            else:
                reslist.append("CodeCup")
for r in reslist:
    print(r)