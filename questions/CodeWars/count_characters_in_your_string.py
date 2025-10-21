# https://www.codewars.com/kata/52efefcbcdf57161d4000091/python
def count(s):
    res = {}
    for i in s:
        if i in res:
            nv = res[i]+1
            res[i] = nv
        else:
            res[i] = 1
    return res