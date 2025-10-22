# https://www.codewars.com/kata/5277c8a221e209d3f6000b56/python
def valid_braces(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif ch in ')]}':
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    
    return not stack