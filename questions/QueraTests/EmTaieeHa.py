# ام تایی ها
# https://quera.org/problemset/76278
def calculator(n, m, li):
    new_list = []
    for i in range(0,n,m):
        if i+m<=n:
            temp_list = (li[i:i+m])
            new_list.append(sum(temp_list))
        else:
            temp_list = (li[i:])
            new_list.append(sum(temp_list))
    sum_new = new_list[0]
    for ii in range(1,len(new_list)):
        if ii%2!=0:
            sum_new-=new_list[ii]
        else:
            sum_new+=new_list[ii]
    return (sum_new)