# problem 44

def pentagonal(n):
    return n * (3 * n - 1) // 2

def is_pentagonal(x):
    n = (1 + (24 * x + 1)**0.5) / 6
    return n.is_integer()

p = []
t = 1
while True:
    p_t = pentagonal(t)
    for pj in p:
        diff = abs(p_t - pj)
        sum_ = p_t + pj
        if is_pentagonal(diff) and is_pentagonal(sum_):
            print("Found:", p_t, pj)
            print("Difference:", diff)
            exit()
    p.append(p_t)
    t += 1