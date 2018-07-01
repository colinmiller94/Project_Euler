def is_prime(n):
    if n== 0 or n == 1:
        return False
    if n == 2:
        return True
    i = 2
    while i**2 <=n:
        if n % i == 0:
            return False
        i += 1
    return True




i = 9

stop = False

while not stop:
    if is_prime(i):
        continue
    j = 2
    sq_term = 2 * j**2
    while sq_term <= i-2:
        sq_term = 2 * j**2
        if not is_prime(i - sq_term):
            print(i)
            stop = True

        j +=1
    print(i)
    i += 2

