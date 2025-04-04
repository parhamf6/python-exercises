# kn = str(input())
# knlist = kn.rsplit(" ")
# k = int(knlist[0])
# n = int(knlist[1])
# h = k
# blist = []
# clist= []
# a = str(input())
# alist = a.rsplit(" ")
# for m in range(h):
#     if k!=-1:
#         indexn = n-1-k
#         valueofi=int(alist[indexn])
#         blist.append(valueofi)
#         k=k-1
#     if k==0:
#         for t in blist :
#             c = int(t)-1
#             clist.append(c)

# sortedlist = sorted(clist)
# if sortedlist[0]==0:
#     print(int(sortedlist[0])+1)
# else :
#     print(int(sortedlist[0]))


def find_nth_person_number(k, n, numbers):
    # Extend the list to ensure it has at least 'n' elements
    while len(numbers) < n:
        # For each new person, determine the smallest number they can take
        current_length = len(numbers)
        if current_length < k:
            look_ahead_range = numbers[:current_length]
        else:
            look_ahead_range = numbers[current_length - k:current_length]
        
        # Convert the range to a set to remove duplicates
        look_ahead_set = set(look_ahead_range)
        
        # Find the smallest missing positive integer
        smallest_number = 1
        while smallest_number in look_ahead_set:
            smallest_number += 1
        
        # Append this smallest number to the list
        numbers.append(smallest_number)
    
    # Return the number of the n-th person in the line
    return numbers[n-1]

# Read inputs
k, n = map(int, input().strip().split())
numbers = list(map(int, input().strip().split()))

# Find and print the number of the n-th person in the line
print(find_nth_person_number(k, n, numbers))
