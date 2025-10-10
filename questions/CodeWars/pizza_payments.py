# https://www.codewars.com/kata/5b043e3886d0752685000009/python
def michael_pays(cost):
    if cost<5:
        return (cost)
    else:
        m = cost*(2/3)
        k = cost*(1/3)
        if k>10:
            o = k - 10
            k = 10
            m+=o
        return m