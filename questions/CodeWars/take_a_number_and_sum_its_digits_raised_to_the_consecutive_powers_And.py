# https://www.codewars.com/kata/5626b561280a42ecc50000d1/python
def sum_dig_pow(a, b):
    res = []
    for i in range(a,b+1):
        if i<10:
            res.append(i)
        else:
            r = 0
            for c in range(1,len(str(i))+1):
                r = r + int(str(i)[c-1])**c
            if r==i:
                res.append(i)
    return res