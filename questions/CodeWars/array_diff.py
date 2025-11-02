# https://www.codewars.com/kata/523f5d21c841566fde000009/python
def array_diff(a, b):
    r = []
    for i in a:
        if i not in b:
            r.append(i)
    return r