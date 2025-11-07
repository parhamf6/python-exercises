# https://www.codewars.com/kata/525b4164eb636fb2f90002a0/python
def numerology(date):
    date_str = f"{date.month:02}{date.day:02}{date.year}"
    total = sum(int(digit) for digit in date_str)
    while total >= 10:
        total = sum(int(digit) for digit in str(total))
    return total