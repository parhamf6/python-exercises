# داروی کرونا
# https://quera.org/problemset/178600
n=int(input())
k=int(input())
p=int(input())
q=int(input())
Sh = n-k
Na = p-q
if Sh>Na:
    print("Shekarestan")
if Sh<Na:
    print("Namakestan")
if Sh==Na:
    print("Equal")