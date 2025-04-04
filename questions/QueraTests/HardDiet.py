s=str(input())
G = s.count("G")
R = s.count("R")
Y = s.count("Y")
if R>=3 or (R>=2 and Y>=2) or G==0:
    print("nakhor lite")
else:
    print("rahat baash")

