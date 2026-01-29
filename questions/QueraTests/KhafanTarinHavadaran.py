# خفن ترین هواداران
# https://quera.org/problemset/176776
s = str(input())
zeroes = s.split("1")
longest = 0
for i in zeroes:
    if len(i)>longest:
        longest=len(i)
print(longest)