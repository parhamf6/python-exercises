# problem 20
f = 1
for i in range(1,101):
    f = f*i
su = 0
for s in str(f):
    su = su + int(s)
print(su)