import math

sta = 1
while sta!=0:
    n = int(input("Enter A number or 0 for quit :"))
    res = []
    if n==0:
        sta=0
        print("Good Luck")
        break
    else:
        for i in range(1, int(math.sqrt(n))+1):
            if n%i==0:
                res.append(i)
                res.append(n//i)
    res.sort()
    x = "".join(str(res))
    print(x)