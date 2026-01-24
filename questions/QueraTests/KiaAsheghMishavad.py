# کیا عاشق میشود
# https://quera.org/problemset/6085
n = int(input())
heights = list(map(int, input().split()))
stack = []
max_counts = {}
for h in heights:
    while stack and stack[-1][0] > h:
        val, count = stack.pop()
        if val in max_counts:
            if count > max_counts[val]:
                max_counts[val] = count
        else:
            max_counts[val] = count
    if stack and stack[-1][0] == h:
        stack[-1] = (h, stack[-1][1] + 1)
    else:
        stack.append((h, 1))
while stack:
    val, count = stack.pop()
    if val in max_counts:
        if count > max_counts[val]:
            max_counts[val] = count
    else:
        max_counts[val] = count
print(max(max_counts.values()))