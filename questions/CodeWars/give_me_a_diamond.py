# https://www.codewars.com/kata/5503013e34137eeeaa001648/python
def diamond(n):
    if n % 2 == 0 or n <= 0:
        return None
    else:
        l = [i for i in range(1, n + 1, 2)]
        um = l[:-1]
        md = l[::-1]
        res = []
        for r in um:
            spaces = (n - r) // 2
            res.append(" " * spaces + "*" * r)
        for r in md:
            spaces = (n - r) // 2
            res.append(" " * spaces + "*" * r)
        return "\n".join(res) + "\n"