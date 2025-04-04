n = int(input())
ch = "*"
w = " "
print(n*ch)
for i in range(n-2):
    print(f"*{w*(n-2)}*")
print(n*ch)