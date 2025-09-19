# https://www.codewars.com/kata/5572392fee5b0180480001ae/python
def computer_to_phone(numbers):
    #your code here
    tr = {
        "1":"7",
        "2":"8",
        "3":"9",
        "7":"1",
        "8":"2",
        "9":"3",
    }
    r = ""
    for i in numbers:
        if i in tr:
            r = r+ tr[i]
        else:
            r = r + i
    return r