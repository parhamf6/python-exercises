# https://www.codewars.com/kata/54d4c8b08776e4ad92000835/python
from math import log
def isPP(n):
    if n < 4:
        return None
    max_k = int(log(n, 2)) + 1
    for k in range(2, max_k + 1):
        m = round(n ** (1 / k))
        if m > 1 and m ** k == n:
            return [m, k]
    return None