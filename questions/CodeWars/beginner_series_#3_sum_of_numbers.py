# https://www.codewars.com/kata/55f2b110f61eb01779000053/python
def get_sum(a,b):
    l= [a,b]
    l.sort()
    r=0
    for i in range(l[0],l[1]+1):
        r+=i
    return r