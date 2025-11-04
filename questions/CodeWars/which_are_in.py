# https://www.codewars.com/kata/550554fd08b86f84fe000a58/python
def in_array(array1, array2):
    a2s = " ".join(array2)
    res = []
    for i in array1:
        if i in a2s and i not in res:
            res.append(i)
    res.sort()
    return res