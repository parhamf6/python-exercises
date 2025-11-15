# https://www.codewars.com/kata/559536379512a64472000053/python
def play_pass(s, n):
    res = []
    alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i, ch in enumerate(s):
        if ch.isalpha():
            idx = alph.index(ch)
            new_ch = alph[(idx + n) % 26]
            new_ch = new_ch if i % 2 == 0 else new_ch.lower()
            res.append(new_ch)
        elif ch.isdigit():
            res.append(str(9 - int(ch)))
        else:
            res.append(ch)
    return "".join(res[::-1])