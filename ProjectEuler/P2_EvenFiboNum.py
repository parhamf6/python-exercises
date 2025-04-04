p = 1
n = 1
s = 0
while n<4000000:
    ins = p+n
    p = n
    n = ins
    if p%2==0:
        s = s + p

print(s)