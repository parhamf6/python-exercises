n = int(input())
names = []
amount = []
higher = 0
for i in range(n):
    x = str(input())
    z = x.rsplit(" ")
    names.append(z[0])
    amount.append(z[-1])
for b in amount:
    if int(b)>int(higher):
        higher = b
indexnum = amount.index(higher)
res = names[int(indexnum)]
print(res)