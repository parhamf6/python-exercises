# https://www.codewars.com/kata/52597aa56021e91c93000cb0
def move_zeros(lst):
    zero = []
    notzero = []
    for i in lst:
        if i==0:
            zero.append(i)
        else:
            notzero.append(i)
    return notzero+zero