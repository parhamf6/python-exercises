k=int(input())
n=1
side = 'p'
while k>=0:
    k = k -n
    if side=='p':
        side='b'
    else:
        side='p'
if side=='p':
    print("Payin Barare")
else:
    print("Bala Barare")