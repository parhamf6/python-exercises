# neckless = int(input())
# for i in range(neckless):
#     user = list(input().split())
#     firste = str(user[0])
#     secend = str(user[1])
#     secrev = secend[::-1]
#     if firste == secrev:
#         print("YES")
#     if firste!=secrev:
#         print("NO")

# First, take the number of inputs
neckless = int(input())

# Create a list to store the inputs
inputs = []

# Then, take all the inputs and store them in the list
for i in range(neckless):
    user = list(input().split())
    inputs.append(user)

# Create a list to store the results
results = []

# Then, iterate over the inputs and perform the operations
for user in inputs:
    firste = str(user[0])
    secend = str(user[1])
    secrev = secend[::-1]
    
    if firste == secrev:
        results.append("YES")
    else:
        results.append("NO")

# Finally, print the results
for result in results:
    print(result)