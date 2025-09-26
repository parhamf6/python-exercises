# https://www.codewars.com/kata/59cd0535328801336e000649/python
def interest(p, r, n):
    s = p * (1+(r*n))
    p = p * ((1+r)**n)
    return [round(s),round(p)]