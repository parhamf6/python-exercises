n = int(input())
nlist = []
for i in range(n):
    x = str(input())
    nlist.append(x)
nlist.sort()
final = 0
for i in nlist:
    indexi = nlist.index(i)
    if i==nlist[0]:
        final = str(i)
    if i!=nlist[-1]:
        n1 = str(i)
        l1 = len(n1)
        n2 = nlist[indexi+1]
        l2 = len(n2)
        dif = l2-l1
        new = n2[dif:]
        sum = new + n2
print(final)





















# final = nlist[0]
# while read<n:
#     if nlist[read]!=nlist[-1]:
#         n1 = nlist[read]
#         n2 = nlist[read+1]
#         l1 = len(n1)
#         l2 = len(n2)
#         dif = l1-l2
#         rest = n1[dif:]
#         sum = int(rest)+int(n2)
#         final = n1[:dif]+str(sum)
#         read = read +1
#         print(final)
#     if nlist[read]==nlist[-1]:
#         n1 = final
#         n2 = nlist[-1]
#         l1 = len(n1)
#         l2 = len(n2)
#         if l1>l2:
#             dif = l1-l2
#             rest = n1[dif:]
#             sum = int(rest)+int(n2)
#             final = final[:dif]+str(sum)
#         read = read +1
        
# print(final)
