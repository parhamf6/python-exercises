# https://www.codewars.com/kata/55c45be3b2079eccff00010f/python
import re
def order(sentence):
    if len(sentence)>0:
        sl = sentence.rsplit(" ")
        r = ["n"]*len(sl)
        for i in sl:
            mat = re.search(r'\d+', i)
            nu = int(mat.group())
            r[nu-1] = i
        return " ".join(r)
    else:
        return ""