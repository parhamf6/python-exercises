# https://www.codewars.com/kata/52c31f8e6605bcc646000082/python
def two_sum(numbers, target):
    for i in range(len(numbers)):
        x = target - numbers[i]
        if x in numbers[i+1:]:
            j = numbers[i+1:].index(x) + (i+1)
            return (i, j)
    return ()