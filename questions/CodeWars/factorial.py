# https://www.codewars.com/kata/54ff0d1f355cfd20e60001fc/python
def factorial(n):
    r = 1
    if n>=0 and n<=12:
        for i in range(1,n+1):
            r = r * i
    elif n<0 or n>12:
        raise ValueError('A very specific bad thing happened')
    return r