s = str(input())
slist = s.rsplit(" ")
n = float(slist[0])
k = float(slist[1])
s = float(slist[-1])
nk = n * k
if nk<=s:
    print("Kafie!")
else:
    print("Na! yeki bayad bere sabzi bekhare")