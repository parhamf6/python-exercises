# بازه ی آزمونی
# https://quera.org/problemset/145639
s = str(input()).split(" ")
ss,ff,ll,xx = int(s[0]), int(s[1]) , int(s[2]), int(s[3])
if xx>=ff:
    print("exam finished!")
elif xx<ss:
    print("exam did not started!")
else:
    enter_time_diff = ff-xx
    if enter_time_diff<ll:
        print(enter_time_diff)
    else:
        print(ll)