n = int(input())
ans = []
for ni in range(1,n):
    if ni%2!=0:
        ans.append(ni)
res = 0
for ansi in ans:
    res = res + ansi
print(res)