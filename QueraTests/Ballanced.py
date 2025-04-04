n = str(input())
o = int(n.count("("))
c = int(n.count(")"))
if o>c:
    x = o-c
    x = x/2
    o = o - x
    c = c + x
    print(int(x))
if o<c:
    x = c-o
    x = x/2
    o = o + x
    c = c - x
    print(int(x))
else :
    print(2)