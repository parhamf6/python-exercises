
def game(x):
    t = 0
    for i in str(x):
        t = abs(t-int(i))
    re = abs(t)
    return(re)


# x = str(input())
# t = 0
# for i in x:
#     t = abs(t-int(i))
# print(abs(t))
