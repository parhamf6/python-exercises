# https://www.codewars.com/kata/5264d2b162488dc400000001/python
def spin_words(sentence):
    w = sentence.split()
    r = []
    for i in w:
        if len(i)>=5:
            r.append(i[::-1])
        else:
            r.append(i)
    return " ".join(r)