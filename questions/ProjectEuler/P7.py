# problem 7
def is_prime(n, primes):
    for p in primes:
        if p * p > n:
            break
        if n % p == 0:
            return False
    return True

prime = [2]
s = 3

while len(prime) < 10001:
    if is_prime(s, prime):
        prime.append(s)
    s += 2  # skip even numbers

print(prime[-1])