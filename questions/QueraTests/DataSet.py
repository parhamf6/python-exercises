# دیتاست
# https://quera.org/problemset/190993
inp = str(input()).split(" ")
nn, qq, ll = int(inp[0]), int(inp[1]), int(inp[2])
saved_binaries = {}
for ni in range(nn):
    nin = str(input()).split(" ")
    saved_binaries[int(nin[0])] = nin[1] 
for qi in range(qq):
    qin = int(input())
    if qin in saved_binaries:
        print(saved_binaries[qin])
    else:
        print("Unknown")