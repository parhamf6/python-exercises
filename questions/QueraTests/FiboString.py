n = int(input())
fibo1 = 1
fibo2 = 1
fibo = [1]
for i in range(n):
    fibo3 = fibo1+fibo2
    fibo.append(fibo3)
    fibo1 = fibo2
    fibo2 = fibo3
s = ""
for j in range(n):
    if (j+1) in fibo:
        s+="+"
    else:
        s+="-"
print(s)