# https://www.codewars.com/kata/57b9fc5b8f5813384a000aa3/python
import re
def calculate(strng):
    s = strng.rsplit(" ")
    ns = re.findall(r'\d+', strng)
    if "loses" in s:
        return int(ns[0])-int(ns[1])
    else:
        return int(ns[0])+int(ns[1])