# https://www.codewars.com/kata/5340298112fa30e786000688/python
def twos_difference(lst): 
    res = []
    for i in lst:
        if i+2 in lst:
            if (i,i+2) not in res:
                res.append((i,i+2))
    res.sort()
    return res