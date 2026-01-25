# ماریو و آنلاین شاپ
# https://quera.org/problemset/193460
s1 = str(input()).split(" ")
s2 = str(input()).split(" ")
rate = int(input())
cm, gm = int(s1[0]), int(s1[1])
cs, gs = int(s2[0]), int(s2[1])
c_diff = cs-cm
g_diff = gs-gs
if c_diff>0 and g_diff<0:
    cm+=abs(int(g_diff*rate))
else:
    gm+=abs(int(c_diff/rate))
print(cm, gm)