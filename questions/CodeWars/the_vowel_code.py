# https://www.codewars.com/kata/53697be005f803751e0015aa/python
def encode(st):
    en = ["a","e","i","o","u"]
    de = ["1","2","3","4","5"]
    res = []
    for i in st:
        r = []
        for si in i:
            if si in en:
                r.append(str(de[en.index(si)]))
            else:
                r.append(si)
        res.append("".join(r))
    return "".join(res)
def decode(st):
    en = ["a","e","i","o","u"]
    de = ["1","2","3","4","5"]
    res = []
    for i in st:
        r = []
        for si in i:
            if (si) in de:
                r.append(str(en[de.index(si)]))
            else:
                r.append(si)
        res.append("".join(r))
    return "".join(res)