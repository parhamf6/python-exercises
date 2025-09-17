# https://www.codewars.com/kata/52dbae61ca039685460001ae/python
def change(st):
    outp = "00000000000000000000000000"
    alph = "abcdefghijklmnopqrstuvwxyz"
    outplist = list(outp)
    for i in st:
        loweri = i.lower()
        if loweri in alph:
            index = alph.rindex(loweri)
            outplist[index] = "1"
    return "".join(outplist)