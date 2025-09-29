# https://www.codewars.com/kata/5810085c533d69f4980001cf/python
def calculator(x,y,op):
    if str(x).isnumeric() and str(y).isnumeric():
        if op == "+":
            return x + y
        elif op == "-":
            return x - y
        elif op == "*":
            return x * y
        elif op == "/":
            return x / y
        else:
            return "unknown value"
    else:
        return "unknown value"