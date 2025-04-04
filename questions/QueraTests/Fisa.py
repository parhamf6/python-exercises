c=int(input())
b=int(input())
a=int(input())

if ((a**2)+(b**2)==(c**2)):
    print("YES")
if ((a**2)+(c**2)==(b**2)):
    print("YES")
if ((c**2)+(b**2)==(a**2)):
    print("YES")
else:
    print("NO")
