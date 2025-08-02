# problem 40
s = ""
n = 1
while len(s)<1000000:
    s = s + str(n)
    n+=1
res = int(s[1-1])*int(s[10-1])*int(s[100-1])*int(s[1000-1])*int(s[10000-1])*int(s[100000-1])*int(s[1000000-1])
print(res)
