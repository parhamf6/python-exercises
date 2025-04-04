MainList = ["shanbe","1shanbe","2shanbe","3shanbe","4shanbe","5shanbe","jome"]
n1 = int(input())
x1  = str(input())
y1  = x1.rsplit(" ")
n2 = int(input())
x2  = str(input())
y2  = x2.rsplit(" ")
n3 = int(input())
x3  = str(input())
y3  = x3.rsplit(" ")
nlist = y1+y2+y3
temp = []
for i in MainList:
    if i not in nlist:
        temp.append(i)

print(len(temp))