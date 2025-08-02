# problem 12
import math

def count_divisors(n):
    count = 0
    sqrt_n = int(math.sqrt(n))
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            count += 2 if i != n // i else 1  # Count both i and n//i, unless they're equal
    return count

n = 1
triangle = 0

while True:
    triangle = n * (n + 1) // 2  # nth triangle number
    if count_divisors(triangle) > 500:
        print(triangle)
        break
    n += 1