largest = 0
count = 0
for i in range(1,1000000):
    t=i
    c= 0
    while t!=1:
        if t%2==0:
            t = t/2
            c+=1
        else:
            t = (3*t)+1
            c+=1
    if c>=count:
        count=c
        largest=i

print(largest)
