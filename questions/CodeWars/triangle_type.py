# https://www.codewars.com/kata/53907ac3cd51b69f790006c5/python
def triangle_type(a, b, c):
    a, b, c = sorted([a, b, c])
    if a + b <= c:
        return 0
    elif c**2 == a**2 + b**2:
        return 2
    elif c**2 > a**2 + b**2:
        return 3
    else:
        return 1