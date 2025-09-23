# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/python
def persistence(n):
    r = 0
    sl = []
    def extractor(ns):
        for i in str(ns):
            sl.append(i)
    extractor(n)
    while len(sl)!=1:
        c = 1
        for i in sl:
            c = c*int(i)
        r+=1
        sl.clear()
        extractor(c)
    return r