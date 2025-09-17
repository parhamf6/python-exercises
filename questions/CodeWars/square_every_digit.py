# https://www.codewars.com/kata/546e2562b03326a88e000020/python
def square_digits(num):
    numstring = str(num)
    res = ""
    for i in numstring:
        x = int(i)**2
        res = res + str(x)
    return int(res)