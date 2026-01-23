# مجید و ماژیک هایش
# https://quera.org/problemset/9109
n = int(input())
sl = str(input()).split(" ")
s = []
for ii in sl:
    s.append(int(ii))
s.sort()
lowest = s.count(s[0])
data = {}
for i in range(n):
    c = s.count(s[i])
    if s[i] not in data:
        data[s[i]] = c
x = sorted(data, key= lambda x:data[x])
print(x[0])