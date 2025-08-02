# problem 25
n1 = 1
n2 = 1
i = 1
while True:
    nn2 = n2
    nn1 = n2
    n2=n1+nn2
    n1 = nn1
    i+=1
    if (len(str(n2)))==1000:
        print(i+1)
        break
