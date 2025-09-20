# https://www.codewars.com/kata/52fba66badcd10859f00097e/python
import re
def disemvowel(string_):
    s = string_
    res = re.sub(r"[aeiouAEIOU]", "", s)
    return res