# https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/python
def sort_array(source_array):
    odd = []
    pre = []
    for i in source_array:
        if i%2==0:
            pre.append(i)
        else:
            pre.append("x")
            odd.append(i)
    odd.sort()
    o = 0
    res = []
    for p in pre:
        if p=="x":
            res.append(odd[o])
            o+=1
        else:
            res.append(p)
    return res