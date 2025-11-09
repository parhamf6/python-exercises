# https://www.codewars.com/kata/52b757663a95b11b3d00062d/python
def to_weird_case(words):
    wl = words.split()
    r = []
    for w in wl:
        res = []
        for i in range(len(w)):
            if i%2==0:
                res.append(w[i].upper())
            else:
                res.append(w[i].lower())
        r.append("".join(res))
    return " ".join(r)