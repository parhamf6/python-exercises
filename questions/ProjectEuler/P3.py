# problem 3
import math
p = []
number = 600851475143
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True
for i in range(1,int(math.sqrt(number))+1):
    if number%i==0:
        if is_prime(i):
            p.append(i)
print(p[-1])