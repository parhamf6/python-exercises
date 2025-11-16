# https://www.codewars.com/kata/5672682212c8ecf83e000050/python
def dbl_linear(n):
    u = [1]
    i2 = i3 = 0
    while len(u) <= n:
        y = 2 * u[i2] + 1
        z = 3 * u[i3] + 1
        if y < z:
            u.append(y)
            i2 += 1
        elif y > z:
            u.append(z)
            i3 += 1
        else:  # y == z
            u.append(y)
            i2 += 1
            i3 += 1
    return u[n]