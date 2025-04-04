n = int(input())
ns = str(input())
slist=ns.rsplit(" ")
for i in slist:
    if int(i)<=3:
        c = "*"
        x = int(i)
        print(f"{x*c}")
    else:
        print("*")