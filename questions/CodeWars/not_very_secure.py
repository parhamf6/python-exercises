# https://www.codewars.com/kata/526dbd6c8c0eb53254000110/python
def alphanumeric(password: str) -> bool:
    cc = 0
    nc = 0
    if " " in password or "_" in password:
        return False
    else:
        for i in password:
            if i.isalpha():
                cc += 1
            elif i.isdigit():
                nc += 1
            else:
                return False
        if cc + nc == 0:
            return False
        else:
            return True