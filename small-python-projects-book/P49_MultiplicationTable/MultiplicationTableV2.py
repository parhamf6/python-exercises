# More advance version

down_range = 10000
up_range = 10010
col_padding = len(str(up_range))
row_padding = len(str(up_range*up_range))
dashes_length = (down_range*up_range)+col_padding+row_padding

for i in range(down_range, up_range+1):
    if i==down_range:
        print(col_padding*" " + "|", end="")
    print(str(i).rjust(row_padding), end="  ")
print()
num_cols = up_range - down_range + 1
print(col_padding*"-" + "+" + ((row_padding+2)*num_cols - 2) * "-")

for n1 in range(down_range, up_range+1):
    print(str(n1).rjust(col_padding), end="")
    print("|", end="")
    for n2 in range(down_range,up_range+1):
        print(str(n1*n2).rjust(row_padding), end="  ")
    print()