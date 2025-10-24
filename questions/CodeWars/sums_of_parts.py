# https://www.codewars.com/kata/5ce399e0047a45001c853c2b/python
def parts_sums(ls):
    res = []
    total = sum(ls)
    for i in range(len(ls)):
        res.append(total)
        total -= ls[i]
    res.append(0)
    return res