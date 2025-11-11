# https://www.codewars.com/kata/51e0007c1f9378fa810002a9/python
def parse(data):
    res = []
    v = 0
    for p in data:
        if p=="i":
            v+=1
        elif p=="d":
            v-=1
        elif p=="s":
            v = v**2
        elif p=="o":
            res.append(v)
    return res