# problem 21

res = []
s = 0
def devisors(n):
    d = []
    suma = 0
    for i in range(1,n):
        if n%i==0:
            d.append(i)
    for c in d:
        suma = suma + c
    return suma
for a in range(1,10000):
    b = devisors(a)
    m = devisors((b))
    if m==a and a!=b:
        res.append(a)
for z in res :
    s = s + z
print(s)