sumsqu = 0
squsum = 0
for i in range(1,101):
    squsum+=i
    sumsqu = sumsqu + (i**2)
print((squsum**2)-sumsqu)