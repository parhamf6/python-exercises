# https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/python
def high(x):
    s = "abcdefghijklmnopqrstuvwxyz"
    xl = x.split(" ")
    top_word = ""
    top_score = 0
    for i in xl:
        c = 0
        for xi in i:
            c+=(s.index(xi.lower())+1)
        if c>top_score:
            top_score=c
            top_word = i
    return top_word