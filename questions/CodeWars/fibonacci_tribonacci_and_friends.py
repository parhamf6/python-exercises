# https://www.codewars.com/kata/556e0fccc392c527f20000c5/python
def xbonacci(signature, n):
    x = len(signature)
    if x==0:
        return []
    elif x>=n:
        return signature[:n]
    else:
        while len(signature)<n:
            temp = 0
            for i in range(x):
                temp+=signature[-1-i]
            signature.append(temp)
        return signature