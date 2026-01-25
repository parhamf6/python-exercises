# پیشگویی خر
# https://quera.org/problemset/4066
nm = str(input()).split(" ")
n, m = int(nm[0]), int(nm[1])
answers = {}
for i in range(n):
    s = str(input()).split(" ")
    answers[s[0]] = s[1]
boz = str(input()).split(" ")
arayeshgar = []
for b in boz:
    if b in answers:
        arayeshgar.append(f"{answers[b]} kachal!")
    else:
        arayeshgar.append("kachal!")
print(" ".join(arayeshgar))