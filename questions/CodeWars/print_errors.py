def printer_error(s):
    valid = "abcdefghijklm"
    e = 0
    for i in s:
        if i not in valid:
            e+=1
    return (f"{e}/{len(s)}")