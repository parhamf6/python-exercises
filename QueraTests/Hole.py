n = str(input())
nlist = n.rsplit(" ")
if n[0]==n[-1]:
    print("Saal Noo Mobarak!")
if n[0]<n[-1]:
    x = int(n[-1])-int(n[0])
    t = "R"*x
    print(t)
if n[0]>n[-1]:
    x = int(n[0])-int(n[-1])
    t = "L"*x
    print(t)
