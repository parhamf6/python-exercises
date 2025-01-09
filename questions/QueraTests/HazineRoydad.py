# برآورد هزینه رویداد
# https://quera.org/problemset/306523
n = int(input())
expenses_sum = 0
for i in range(n):
    n2 = (input())
    n2_list = n2.split(" ")
    s, c = int(n2_list[0]), int(n2_list[1])
    expenses_sum+=(s*c)
print(expenses_sum)