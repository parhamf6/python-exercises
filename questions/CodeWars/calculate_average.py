# https://www.codewars.com/kata/57a2013acf1fa5bfc4000921
def find_average(numbers):
    sum = 0
    for i in numbers:
        sum += i
    if len(numbers) == 0:
        return 0
    else:
        return sum / len(numbers)