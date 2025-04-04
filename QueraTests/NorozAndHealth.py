x = int(input())
n = int(input())
res = 0
if n==7:
    res = x
elif n==0:
    res = 20
elif 0<n<7 or n>7:
    for i in range(n):
        x = x - 1
    res = x
if res<0:
    res = 0
print(res)