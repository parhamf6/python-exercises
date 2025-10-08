# https://www.codewars.com/kata/545cedaa9943f7fe7b000048/python
def is_pangram(st):
    al = 'abcdefghijklmnopqrstuvwxyz'
    r = []
    for i in st:
        if i.lower() in al:
            if i.lower() not in r:
                r.append(i.lower())
    if len(r)>=26:
        return True
    else:
        return False