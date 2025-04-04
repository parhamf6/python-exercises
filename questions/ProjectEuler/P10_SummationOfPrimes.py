def sum_of_primes(limit):
    # Step 1: Create a list to represent whether each number is prime
    sieve = [True] * limit  # Assume all numbers are prime initially
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers

    # Step 2: Start marking multiples of each prime number
    for i in range(2, int(limit**0.5) + 1):  # Only go up to sqrt(limit)
        if sieve[i]:  # If i is still marked as prime
            for j in range(i * i, limit, i):  # Mark all multiples of i as non-prime
                sieve[j] = False

    # Step 3: Sum all indices that are still marked as prime
    return sum(i for i, is_prime in enumerate(sieve) if is_prime)

result = sum_of_primes(2000000)
print(result)
