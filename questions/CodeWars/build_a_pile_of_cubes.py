def find_nb(m):
    n = 1
    s = 0
    while s < m:
        s = s + (n**3)
        n+=1
    if s>m:
        return -1
    else:
        return n-1