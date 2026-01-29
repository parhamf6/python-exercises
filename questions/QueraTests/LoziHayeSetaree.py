# لوزی های ستاره ای
# https://quera.org/problemset/9773
n = int(input())
empty_space_start = n-1
star_space_start = 1
star_lines = []
upper_half = True
for i in range(n):
    sp = " "
    star = "*"
    star_line = f"{int(empty_space_start/2)*sp}{star*star_space_start}{empty_space_start*sp}{star*star_space_start}{int(empty_space_start/2)*sp}"
    star_lines.append(star_line)
    if star_space_start==n:
        upper_half = False
    if upper_half:
        empty_space_start-=2
        star_space_start+=2
    elif not upper_half:
        empty_space_start+=2
        star_space_start-=2
for p in star_lines:
    print(p)
        
