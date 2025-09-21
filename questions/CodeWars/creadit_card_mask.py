# https://www.codewars.com/kata/5412509bd436bd33920011bc/python
# return masked string
def maskify(cc):
    if len(cc)>4:
        last = cc[-4:]
        i = "#"
        masked = f"{(len(cc)-4)*i}{last}"
        return masked
    return cc