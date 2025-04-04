t=int(input())
for i in range(t):
    data=input()
    listd= data.rsplit(" ")
    a = int(listd[0])
    b = int(listd[1])
    h = int(listd[2])
    tot = 0
    timet = 0
    while tot<h:
        tot = tot+a
        timet = timet + 1
        if tot<h:
            tot=tot-b
        if tot>=h:
            print(timet)
            break
