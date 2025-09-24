# https://www.codewars.com/kata/68c7c3cb12252d313dc9fd8b/python
def is_palindrome(n: int) -> bool:
    binary = bin(n)[2:]
    return binary == binary[::-1]