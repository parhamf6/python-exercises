# https://www.codewars.com/kata/54c27a33fb7da0db0100040e/python
import math
def is_square(n):
    if n<0:
        return False
    else:
        s = math.sqrt(n)
        if s==float(int(s)):
            return True
        else:
            return False