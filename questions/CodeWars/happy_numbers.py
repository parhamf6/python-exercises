# https://www.codewars.com/kata/5464cbfb1e0c08e9b3000b3e/python
def is_happy(n):
    r = [n]
    stat = False
    while not stat:
        if r[-1]==1:
            stat = True
        else:
            s = 0
            for c in str(r[-1]):
                s+=int(c)**2
            if s not in r:
                r.append(s)
            else:
                stat = False
                break
    return stat