n =  int(input())
l = []
while n!=0:
    l.append(n)
    n = int(input())

if n==0:
    l.reverse()
    for i in l:
        print(i)