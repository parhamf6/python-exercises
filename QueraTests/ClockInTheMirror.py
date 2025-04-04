n = str(input())
nlist = n.rsplit(" ")
h1 = 12- int(nlist[0])

m1 = 60-int(nlist[-1])
if h1>=12:
    h1 = h1 - 12
if m1>=60:
    m1 = m1-60
print(f"{h1:02}:{m1:02}")