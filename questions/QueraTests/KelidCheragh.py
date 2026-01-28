# کلید چراغ
# https://quera.org/problemset/49028
n = int(input())
first_state = int(input())
state_list = [first_state]
count = 0
for i in range(n-1):
    new_state = int(input())
    if new_state!=state_list[-1]:
        count+=1
    state_list.append(new_state)
print(count)