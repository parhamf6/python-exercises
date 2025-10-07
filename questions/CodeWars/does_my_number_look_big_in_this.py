# https://www.codewars.com/kata/5287e858c6b5a9678200083c/python
def narcissistic( value ):
    l = len(str(value))
    r = 0
    for i in str(value):
        r = r + ((int(i)**l))
    if r==value:
        return True
    else:
        return False