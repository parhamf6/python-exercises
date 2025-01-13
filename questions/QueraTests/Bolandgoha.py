# بلندگوها
# https://quera.org/problemset/3430
s = str(input())
alph_list = []
for a in s:
    alph_list.append(a)
for i in range(1,len(s)+1):
    alph = alph_list[0]
    alph_list.remove(alph)
    how_many = len(s)-len(alph_list)
    alph_list_str = "".join(alph_list)
    print(f"{how_many*alph}{alph_list_str}")
    