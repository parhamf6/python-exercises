# https://www.codewars.com/kata/5324945e2ece5e1f32000370/python
def sum_strings(x, y):
    if not x:
        return y or "0"
    if not y:
        return x or "0"
    x, y = x.lstrip('0') or "0", y.lstrip('0') or "0"
    max_len = max(len(x), len(y))
    x = x.zfill(max_len)
    y = y.zfill(max_len)
    carry = 0
    result = []
    for i in range(max_len - 1, -1, -1):
        digit_sum = int(x[i]) + int(y[i]) + carry
        carry = digit_sum // 10
        result.append(str(digit_sum % 10))
    if carry:
        result.append(str(carry))
    return ''.join(reversed(result))