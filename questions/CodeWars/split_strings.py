# https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/python
def solution(s):
    if len(s)%2 != 0:
        s+="_"
    res = []
    for i in range(0,len(s),2):
        res.append(s[i:i+2])
    return res