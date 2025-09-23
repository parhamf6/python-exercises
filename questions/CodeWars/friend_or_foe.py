# https://www.codewars.com/kata/55b42574ff091733d900002f/python
def friend(x):
    res = []
    for i in x:
        if len(i)==4:
            res.append(i)
    return res