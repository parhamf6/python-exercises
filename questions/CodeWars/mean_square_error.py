# https://www.codewars.com/kata/51edd51599a189fe7f000015/python
def solution(array_a, array_b):
    c = 0
    for i in range(len(array_a)):
        s = array_a[i]-array_b[i]
        c = c + (abs(s**2))
    return c/len(array_a)