# https://www.codewars.com/kata/5541f58a944b85ce6d00006a/python
def product_fib(p):
    fib = [0,1]
    go = True
    while go:
        if fib[-1]*fib[-2]==p:
            return [fib[-2],fib[-1],True]
            break
        if fib[-1]*fib[-2]>p:
            return [fib[-2],fib[-1],False]
            break
        else:
            new = fib[-1]+fib[-2]
            fib.append(new)