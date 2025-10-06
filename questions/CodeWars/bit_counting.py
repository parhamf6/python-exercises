# https://www.codewars.com/kata/526571aae218b8ee490006f4/python
def count_bits(n):
    b = bin(n)
    return b.count('1')