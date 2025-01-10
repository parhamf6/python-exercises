n =  int(input())
li = []
while n!=0:
    li.append(n)
    n = int(input())

if n==0:
    li.reverse()
    for i in li:
        print(i)