user = list(input().split())
user1 = int(user[1])
user2 = int(user[2])
user3 = int(user[3])
user4 = int(user[4])
x = 0
for i in range(1 , (int(user[0]) + 1)):
    if i%user1 == 0 or i%user3 == 0 or i%user4 == 0 or i%user2 == 0:
        x+=1
print(x)