# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/python
def duplicate_encode(word):
    word=word.lower()
    r=[]
    for i in word:
        if word.count(i) == 1:
            r.append('(')
        else:
            r.append(')')
    return ''.join(r)