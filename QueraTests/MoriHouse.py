user = list(input().split())
a = int(user[0])
b = int(user[1])
while a >=b:
    a-=b
    if a < b:
        print(a)
        break
    if a == b:
        print(0)
        break