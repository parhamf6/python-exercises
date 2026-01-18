# مجزا
# https://quera.org/problemset/129726
def separator(ls):
    even = []
    odd = []
    for i in ls:
        if abs(i)%2==0:
            even.append(i)
        else:
            odd.append(i)
    return (even,odd)