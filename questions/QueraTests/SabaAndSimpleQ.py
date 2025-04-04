nk = str(input())
nklist = nk.rsplit(" ")
n = int(nklist[0])
k = int(nklist[-1])
for i in range(k):
    n = n // 2
# if n>=0:
#     print(int(n))
# if n<0:
#     print(int(n)-1)
print(n)