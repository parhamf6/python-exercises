# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/python
def accum(st):
    res_list = []
    for i in range(len(st)):
        res_list.append((f"{st[i]*(i+1)}").capitalize())
    return ("-".join(res_list))