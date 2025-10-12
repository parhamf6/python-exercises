# https://www.codewars.com/kata/56b7251b81290caf76000978/python
def get_last_digit(index):
    f = 0 
    l = 1
    for i in range(1,index+1):
        fn = l
        ln = f+l
        f = fn
        l = ln
    return f%10