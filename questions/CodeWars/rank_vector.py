# https://www.codewars.com/kata/545f05676b42a0a195000d95/python
def ranks(a):
    sorted_unique = sorted(set(a), reverse=True)
    rank_map = {}
    rank = 1
    for val in sorted_unique:
        rank_map[val] = rank
        count = a.count(val)
        rank += count 
    return [rank_map[x] for x in a]