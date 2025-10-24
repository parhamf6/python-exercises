# https://www.codewars.com/kata/52761ee4cffbc69732000738/python
def good_vs_evil(good, evil):
    g = 0
    e = 0
    gs = [1,2,3,3,4,10]
    es = [1,2,2,2,3,5,10]
    gl = good.split(" ")
    el = evil.split(" ")
    for gi in range(len(gl)):
        g = g + int(gl[gi])*gs[gi]
    for ei in range(len(el)):
        e = e + int(el[ei])*es[ei]
    if g>e:
        return "Battle Result: Good triumphs over Evil"
    elif e>g:
        return "Battle Result: Evil eradicates all trace of Good"
    else:
        return "Battle Result: No victor on this battle field"