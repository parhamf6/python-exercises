# https://www.codewars.com/kata/558fc85d8fd1938afb000014/python
def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]