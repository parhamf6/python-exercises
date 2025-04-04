n1=str(input())
n2=str(input())
m1=int(n1[::-1])
m2=int(n2[::-1])
if m1>m2:
    print(f"{n2} < {n1}")
if m2>m1:
    print(f"{n1} < {n2}")
if m2==m1:
    print(f"{n1} = {n2}")