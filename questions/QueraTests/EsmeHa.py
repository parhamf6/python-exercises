# اسم ها
# https://quera.org/problemset/2529
n = int(input())
unique_alphs_len = []
for i in range(n):
    s = str(input())
    unique_alph = []
    for ii in s:
        if ii not in unique_alph:
            unique_alph.append(ii)
    unique_alphs_len.append(len(unique_alph))
unique_alphs_len.sort()
print(unique_alphs_len[-1])