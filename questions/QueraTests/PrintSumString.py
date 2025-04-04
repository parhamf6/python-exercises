n = int(input())
stg = '1'
s = 1
if n>1:
    for i in range(2,n+1):
        # print(i)
        if i!=n:
            stg = stg + f' + {i}'
            s = s + i
        else:
            s = s + i
            stg = stg + f' + {i}'
            print(f"{stg} = {s}")
        # print(s)
else:
    print('1 = 1')