# https://www.codewars.com/kata/54ff3102c1bad923760001f3/python
def get_count(sentence):
    c = 0
    alph = "aeiou"
    for i in sentence:
        if i in alph:
            c+=1
    return c