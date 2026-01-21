# مربا های و مشکلات اقتصادی
# https://quera.org/problemset/20249
nk = str(input()).split(" ")
n, k = int(nk[0]), int(nk[1])
s = str(input()).split(" ")
max_store = n*k
sum_s = 0
for i in s:
    sum_s+=int(i)
    if sum_s>=max_store:
        break
print((max_store-sum_s)//k)