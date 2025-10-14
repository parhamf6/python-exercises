# https://www.codewars.com/kata/520b9d2ad5c005041100000f/python
def pig_it(text):
    tl = text.rsplit(" ")
    r = []
    for i in tl:
        if i.isalpha():
            f = i[0]+"ay"
            l = i[1::]
            r.append(l+f)
        else:
            r.append(i)
    return " ".join(r)