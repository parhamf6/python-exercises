# https://www.codewars.com/kata/576757b1df89ecf5bd00073b/python
def tower_builder(n_floors):
    max = (n_floors*2)-1
    res = []
    for i in range(1,n_floors+1):
        f = (i*2)-1
        e = int((max-f)/2)
        s = "*"*f
        sp = " "*e
        res.append(f"{sp}{s}{sp}")
    return res