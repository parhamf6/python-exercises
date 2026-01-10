# تست بینایی
# https://quera.org/problemset/2659
n = int(input())
main = str(input())
given = str(input())
count_mistake = 0
for i in range(n):
    if main[i]!=given[i]:
        count_mistake+=1
print(count_mistake)