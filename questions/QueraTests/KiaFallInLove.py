# n = int(input())
# s = str(input())
# slist = s.rsplit(" ")
# x = slist[0]
# f = 1
# read = 0
# while read<n:
#     if x==slist[read+1]:
#         f = f +1
#     if x>slist[read+1]:
#         break
#     read = read + 1
# print(f)

# Read input values
n = int(input())
s = input().split()

# Convert flower heights to a list of integers
flower_heights = list(map(int, s))

# Initialize the first flower's height and the count of picked flowers
first_flower_height = flower_heights[0]
count = 1

# Iterate through the flowers starting from the second one
for i in range(1, n):
    if flower_heights[i] >= first_flower_height:
        count += 1
    else:
        break

print(count)
