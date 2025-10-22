# https://www.codewars.com/kata/5842df8ccbd22792a4000245/python
def expanded_form(num):
    res = []
    num = str(num)
    for i in range(len(num)):
        if int(num[i])>0:
            nz = len(num)-i-1
            c = "0"
            res.append(num[i]+f"{c*nz}")
    return " + ".join(res)