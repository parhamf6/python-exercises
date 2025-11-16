# https://www.codewars.com/kata/54d81488b981293527000c8f/python
def sum_pairs(ints, target):
    seen = set()
    for num in ints:
        complement = target - num
        if complement in seen:
            return [complement, num]
        seen.add(num)
    return None