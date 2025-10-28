# https://www.codewars.com/kata/52fb87703c1351ebd200081f/python
def what_century(year):
    year = int(year)
    century = (year - 1) // 100 + 1
    if 11 <= century % 100 <= 13:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(century % 10, "th")
    return f"{century}{suffix}"