n = str(input())
nlist = n.rsplit(" ")
x1 = nlist[0]
y1 = nlist[1]
x2 = nlist[2]
y2 = nlist[3]
if x1==x2 and y1!=y2:
    print("Vertical")
if y1==y2 and x1!=x2:
    print("Horizontal")
if x1!=x2 and y1!=y2:
    print("Try again")
