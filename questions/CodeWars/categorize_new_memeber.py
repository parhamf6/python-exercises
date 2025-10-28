# https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa/python
def open_or_senior(data):
    res = []
    for i in data:
        if i[0] >= 55 and i[-1] > 7:
            res.append('Senior')
        else:
            res.append('Open')
    return res