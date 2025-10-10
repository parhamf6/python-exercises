# https://www.codewars.com/kata/585eaef9851516fcae00004d/python
def what_list_am_i_on(actions):
    na = 0
    ni = 0
    na_list = ["b", "f", "k"]
    ni_list = ["g", "s", "n"]
    for i in actions:
        f = i[0]
        if f in na_list:
            na+=1
        elif f in ni_list:
            ni+=1
    if na>=ni:
        return "naughty"
    else:
        return "nice"