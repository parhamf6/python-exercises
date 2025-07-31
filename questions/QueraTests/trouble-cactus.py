n = int(input())
s = str(input())
sl = s.rsplit(" ")
for i in sl:
    i = int(i)
    if i<=3:
        print("*"*i)
    else:
        print("*")