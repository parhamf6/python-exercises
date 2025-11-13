# https://www.codewars.com/kata/59c633e7dcc4053512000073/python
import re
def solve(s):
    parts = re.split('[aeiou]+', s)
    res = []
    for i in parts:
        t = 0
        if i!="":
            for c in i:
                t+=ord(c)-96
            res.append(t)
    res.sort()
    return res[-1]