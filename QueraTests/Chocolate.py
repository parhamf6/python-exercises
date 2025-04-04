s = str(input())
slist = s.split(" ")
n = int(slist[0])
k = int(slist[1])
if n%k==0:
    print("YES")
else:
    print("NO")