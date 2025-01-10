# اول بینی
# https://quera.org/problemset/649
import math
a = int(input())
b = int(input())
primes = []
def is_prime(n): 
    if n <= 1: 
        return False
  
    max_div = math.floor(math.sqrt(n)) 
    for i in range(2, 1 + max_div): 
        if n % i == 0: 
            return False
    return True
for i in range(a+1,b):
    prime_state = is_prime(i)
    if prime_state:
        primes.append(str(i))
print(",".join(primes))