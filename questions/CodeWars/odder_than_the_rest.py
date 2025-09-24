# https://www.codewars.com/kata/5983cba828b2f1fd55000114/python
def odd_one(arr):
    for i in range(len(arr)):
        if abs(arr[i]) % 2 != 0:
            return i
    return -1