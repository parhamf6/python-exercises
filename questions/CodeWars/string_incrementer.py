# https://www.codewars.com/kata/54a91a4883a7de5d7800009c/python
def increment_string(s):
    if len(s) > 0:
        if s[-1].isdigit():
            i = len(s) - 1
            while i >= 0 and s[i].isdigit():
                i -= 1
            head = s[:i + 1]
            tail = s[i + 1:]
            new_num = str(int(tail) + 1).zfill(len(tail))
            s = head + new_num
        else:
            s += "1"
        return s
    else:
        return "1"