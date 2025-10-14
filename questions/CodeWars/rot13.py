# https://www.codewars.com/kata/530e15517bc88ac656000716/python
def rot13(message):
    alph = "abcdefghijklmnopqrstuvwxyz"
    alphc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    r = ""
    for i in message:
        if i in alph:
            ii = alph.index(i) + 13
            if ii>=26:
                ii-=26
                r+=alph[ii]
            else:
                r+=alph[ii]
        elif i in alphc:
            ii = alphc.index(i) + 13
            if ii>=26:
                ii-=26
                r+=alphc[ii]
            else:
                r+=alphc[ii]
        else:
            r+=i
    return r