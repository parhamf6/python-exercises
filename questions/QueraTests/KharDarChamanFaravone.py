# خر در چمن فراوونه
# https://quera.org/problemset/4065
s = str(input()).split(" ")
a, b, n = int(s[0]), int(s[1]), int(s[2])
if n%2==0:
    print((a+b)*(n//2))
else:
    print((a+b)*(n//2)+a)
