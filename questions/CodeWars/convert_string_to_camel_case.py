# https://www.codewars.com/kata/517abf86da9663f1d2000003/python
import re
def to_camel_case(text):
    if len(text)>0:
        t = re.split(r"[_-]",text)
        res = []
        for i in range(len(t)):
            if i==0:
                res.append(t[i])
            else:
                res.append(t[i].capitalize())
        return "".join(res)
    else:
        return text