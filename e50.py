
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    i = 2
    while i**2 <=n:
        if n % i == 0:
            return False
        i += 1
    return True

primes = []

for i in range(1,10**6):
    print(i)
    if is_prime(i):
        primes.append(i)

max = 0
for index, prime in enumerate(primes):
    total = prime
    max_i = 0
    start = 0


    while start < index:
        total -= primes[start]
        start+=1
        if total == 0:
            if start >


