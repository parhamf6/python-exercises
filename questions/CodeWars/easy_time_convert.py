# https://www.codewars.com/kata/5a084a098ba9146690000969/python
def time_convert(num):
    if num>0:
        h = num//60
        m = num-(h*60)
        return f"{h:02d}:{m:02d}"
    else:
        return "00:00"