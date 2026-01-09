nk = str(input()).split(" ")
n,k  = int(nk[0]), int(nk[1])
stocks = str(input()).split(" ")
ii = 0

k_sum=0
for ik in range(1,k+1):
    k_sum+=ik

for i in range(n-k+1):
    sum = 0
    k_list = stocks[i:i+k]
    for ik in range(k):
        sum+=int(k_list[ik])*(ik+1)
    print(sum/k_sum)

# while ii<n-k+1:
#     sum = 0
#     k_list = stocks[ii:ii+k]
#     for i in range(k):
#         sum+=int(k_list[i])*(i+1)
#     ii+=1
#     print(sum/k_sum)