# https://www.codewars.com/kata/554ca54ffa7d91b236000023/python
def delete_nth(order,max_e):
    r = []
    for i in order:
        if r.count(i) < max_e:
            r.append(i)
    return r