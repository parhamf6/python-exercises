# مثلث خیام
# https://quera.org/problemset/595
n = int(input())
pascal = [["1"], ["1","1"]]
if n>2:
    for i in range(3,n+1):
        temp_row = ["1"]
        for tr in range(i-2):
            temp_row.append(str((int(pascal[-1][tr])+int(pascal[-1][tr+1]))))
        temp_row.append("1")
        pascal.append(temp_row)
for i in range(n):
    print(" ".join(pascal[i]))