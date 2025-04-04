word = str(input())
ans = 1
for i in word:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        ans =  ans * 2
print(ans)