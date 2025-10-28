# https://www.codewars.com/kata/55eeddff3f64c954c2000059/python
def sum_consecutives(lst):
    res = []
    last = lst[0]
    s = last

    for i in lst[1:]:
        if i == last:
            s += i
        else:
            res.append(s)
            last = i
            s = i
    res.append(s)
    return res