# https://www.codewars.com/kata/54d3bb4dfc75996c1c000c6d/python
def midpoint_sum(ints):
    if len(ints)<=2:
        return -1
    else:
        x = -1
        for i in range(1,len(ints)-1):
            if sum(ints[:i])==sum(ints[i+1:]):
                x = i
        return x