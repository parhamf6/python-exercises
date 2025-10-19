# https://www.codewars.com/kata/585d7d5adb20cf33cb000235/python
def find_uniq(arr):
    arr.sort()
    if arr[0]!=arr[-1]:
        if arr[0]==arr[1]:
            return arr[-1]
        else:
            return arr[0]