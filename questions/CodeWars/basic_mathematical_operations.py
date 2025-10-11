# https://www.codewars.com/kata/57356c55867b9b7a60000bd7
def basic_op(operator, value1, value2):
    if operator == "+":
        return value1 + value2
    elif operator == "*":
        return value1 * value2
    elif operator == "-":
        return value1 - value2
    else:
        return value1 / value2