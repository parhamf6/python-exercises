# First, take the number of inputs
moves = int(input())

# Create a list to store the inputs
inputs = []

# Then, take all the inputs and store them in the list
for i in range(moves):
    user = list(input().split())
    inputs.append(user)

# Create a list to store the results
results = []
x = 0
# Then, iterate over the inputs and perform the operations
for user in inputs:
    first = int(user[0])
    secend = int(user[1])
    moved = first - secend
    x +=moved
print(user[0])
