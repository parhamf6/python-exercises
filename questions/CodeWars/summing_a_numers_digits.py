# https://www.codewars.com/kata/52f3149496de55aded000410/python
def sum_digits(number):
    r = 0
    for i in str(abs(number)):
        r+=int(i)
    return r