n = int(input("ENter The Nth Number of the fibonachi sequence : "))
o = 0
t = 1
ans = ["0","1"]
for i in range(n-2):
    if i>0:
        z = t
        t = t + o
        o = z
    ans.append(str(o+t))
print(" ,".join(ans))


