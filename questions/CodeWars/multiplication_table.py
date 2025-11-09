# https://www.codewars.com/kata/534d2f5b5371ecf8d2000a08/python
def multiplication_table(size):
    r = []
    for i in range(1,size+1):
        c = []
        for s in range(1,size+1):
            c.append(s*i)
        r.append(c)
    return r