# https://www.codewars.com/kata/55fd2d567d94ac3bc9000064/python
def row_sum_odd_numbers(n):
    if n==1:
        return 1
    else:
        fn = (n*(n-1))+1
        ln = fn+((n-1)*2)
        s = 0
        for i in range(fn,ln+1,2):
            s+=i
        return s
    # simpler version is only return n**3 :)