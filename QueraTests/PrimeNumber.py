# a = int(input())
# b = int(input())
# for i in range(a,b+1):
#     if i!=1:
#         temp = []
#         temp.append(i%i)
#         if i!=2 :
#             temp.append(i%2)
#         if i!=3 :
#             temp.append(i%3)
#         if i!=4 :
#             temp.append(i%4)
#         if i!=5 :
#             temp.append(i%5)
#         if i!=6 :
#             temp.append(i%6)
#         if i!=7 :
#             temp.append(i%7)
#         if i!=8 :
#             temp.append(i%8)
#         if i!=9 :
#             temp.append(i%9)
#         z = temp.count(0)
#         if z==1:
#             print(i)

a = int(input())
b = int(input())

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

for i in range(a, b + 1):
    if is_prime(i):
        print(i)
