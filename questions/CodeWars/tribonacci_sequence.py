# https://www.codewars.com/kata/556deca17c58da83c00002db/python
def tribonacci(signature, n):
    if n==0:
        return []
    elif n>=3:
        for i in range(n-3):
            l = signature[-1]
            s = signature[-2]
            t = signature[-3]
            tls = l+s+t
            signature.append(tls)
        return signature
    else:
        return signature[:n]