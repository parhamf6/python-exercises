n = int(input())
ans = []
for i in range(n):
    s = str(input())
    r = int(s[1:3], 16)
    g = int(s[3:5], 16)
    b = int(s[5:7], 16)
    rs = 255 - r
    gs = 255 - g
    bs = 255 - b
    hex_color = "#{:02X}{:02X}{:02X}".format(rs, gs, bs)
    ans.append(hex_color)

for i in ans:
    print(i)