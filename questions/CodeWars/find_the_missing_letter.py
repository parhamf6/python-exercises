# https://www.codewars.com/kata/5839edaa6754d6fec10000a2/python
def find_missing_letter(chars):
    a = "abcdefghijklmnopqrstuvwxyz"
#     ac = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(chars)):
        if i!=len(chars)-1:
            cc = chars[i].lower()
            nc = chars[i+1].lower()
            ca = a.index(cc)
            na = a[ca+1]
            if na!=nc:
                if chars[0].isupper():
                    return na.upper()
                else:
                    return na
