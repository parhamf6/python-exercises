print('  |  0    1    2    3    4    5    6    7    8    9   10   11   12')
print('--+---------------------------------------------------------------')
for n1 in range(0,13):
    print(str(n1).rjust(2), end="")
    print("|", end="")
    for n2 in range(0,13):
        print(str(n1*n2).rjust(3), end="  ")
    print()