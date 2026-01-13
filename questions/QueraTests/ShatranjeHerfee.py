# شطرنج حرفه ای
# https://quera.org/problemset/2636
s = str(input()).split()
valid = [1,1,2,2,2,8]
diff = []
for i in range(len(s)):
    diff.append(str(valid[i]-int(s[i])))
print(" ".join(diff))