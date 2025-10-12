# https://www.codewars.com/kata/56b7771481290cc283000f28/python
def last_fib_digit(n):
    n %= 60
    f, l = 0, 1
    for _ in range(n):
        f, l = l, (f + l) % 10
    return f