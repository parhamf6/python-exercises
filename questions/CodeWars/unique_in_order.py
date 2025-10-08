# https://www.codewars.com/kata/54e6533c92449cc251001667/python
def unique_in_order(sequence):
    if len(sequence)>0:
        r = [sequence[0]]
        for i in sequence:
            if i!=r[-1]:
                r.append(i)
    else:
        return []
    return r