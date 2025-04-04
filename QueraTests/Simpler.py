import decimal
n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
thelist = [n1,n2,n3,n4]
sortedlist = sorted(thelist)
sum = (n1+n2+n3+n4)
ave = (sum/4)
mult = (n1*n2*n3*n4)
max = (sortedlist[3])
min = (sortedlist[0])
Sum = f'Sum : {sum:.6f}'
Ave = f'Average : {ave:.6f}'
Mult = f'Product : {mult:.6f}'
Max = f'MAX : {max:.6f}'
Min = f'MIN : {min:.6f}'
finallist=[Sum,Ave,Mult,Max,Min]
for i in finallist:
    print(i)
