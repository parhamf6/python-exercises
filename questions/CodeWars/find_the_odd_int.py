# https://www.codewars.com/kata/54da5a58ea159efa38000836
def find_it(seq):
    res = {}
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i