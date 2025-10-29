# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/python
def snail(array):
    result = []
    while array:
        result += array.pop(0)
        if array and array[0]:
            for row in array:
                result.append(row.pop())
        if array:
            result += array.pop()[::-1]
        if array and array[0]:
            for row in array[::-1]:
                result.append(row.pop(0))
    return result