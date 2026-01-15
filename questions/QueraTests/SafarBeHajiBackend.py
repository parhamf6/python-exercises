# سفر به حاجی بکنده
# https://quera.org/problemset/275137
nk = str(input())
nk_list = nk.split(" ")
n, k = int(nk_list[0]), int(nk_list[1])+1
s_list = []
for ni in range(n):
    nii = str(input())
    nii_list = nii.split(" ")
    s_list.append(nii_list)
villa_expense = []
for i in s_list:
    a = int(i[0])
    b = int(i[1])
    x = int(i[2])
    expense = 0
    expense+=a*x
    if k>x:
        expense+=(k-x)*b
    villa_expense.append(expense)
min_expense = villa_expense[0]
for ei in villa_expense:
    if ei<min_expense:
        min_expense=ei
print(villa_expense.index(min_expense)+1)