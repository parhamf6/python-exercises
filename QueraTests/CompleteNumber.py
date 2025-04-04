import math
x = int(input())
def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor
# def get_divisors(n):
#     for i in range(1, int(n / 2) + 1):
#         if n % i == 0:
#             yield i
#     yield n
# print(list(get_divisors(6)))
dlist = list(divisorGenerator(x))
dlist.remove(x)
res = 0
for i in dlist:
    res = res + int(i)
if res==x:
    print("YES")
else:
    print("NO")
