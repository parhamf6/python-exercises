# https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/python
def filter_list(l):
    res=[]
    for i in l:
        if isinstance(i,int):
            res.append(i)
    return res