# https://www.codewars.com/kata/5514e5b77e6b2f38e0000ca9/python
def up_array(arr):
    r = []
    for i in arr :
        if i<10 and i>=0:
            r.append(str(i))
    if len(r)==0 or len(r)<len(arr):
        return None
    else:
        if len(r)==1 and r[0]=="0":
            return [int(r[0])+1]
        else:
            zero = []
            for z in range(len(r)):
                if r[z]!="0":
                    break
                else:
                    zero.append(0)
            x = int("".join(r))+1
            res = []
            for xi in str(x):
                res.append(int(xi))
            return zero+res