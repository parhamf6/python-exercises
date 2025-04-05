import random


months = ["Jan","Feb","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec","Mar"]
people = int(input("How many people should i generate ? : (Max 100)"))

times = 0

for i in range(10000):
    birthday = []
    for i in range(people):
        mon = str(random.choice(months))
        day =  str(random.randint(1,365))
        appe = mon + day
        birthday.append(appe)
    for c in birthday:
        if birthday.count(c)>1:
            times+=birthday.count(c)
    if i%1000==0:
        print(f"Simulations Runs {i} times")

print((times/(people*10000))*100)