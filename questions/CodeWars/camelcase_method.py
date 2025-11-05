# https://www.codewars.com/kata/587731fda577b3d1b0001196/python
def camel_case(s):
    words = s.split()
    res = []
    for i in words:
        res.append(i.title())
    return "".join(res)