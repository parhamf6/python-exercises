# همایش زندگی بهتر
# https://quera.org/problemset/10325
s = str(input()).split(" ")
r, c = int(s[0]), int(s[1])
rows_down = 10-r+1
if c>10:
    seat_side = 20-c+1
    print(f"Left {rows_down} {seat_side}")
else:
    seat_side = 0+c
    print(f"Right {rows_down} {seat_side}")