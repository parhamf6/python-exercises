n =  int(input())
r = 2*n+1
c = 1
z = 2*n+1
for i in range(1,r+1):
    w = int((c-i)/2)
    wh = " "
    print(f"{" "*w}{"*"*c}{" "*w}")
    z-=2
    if i<=int(r/2):
        c+=2
    else:
        c-=2
        z+=4