# https://www.codewars.com/kata/5552101f47fc5178b1000050/python
def dig_pow(n, p):
    r = 0
    for i in str(n):
        r = r + (int(i)**p)
        p+=1
    ans = r/n
    if ans==float(int(ans)):
        return ans
    else:
        return -1
            