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




i = 9

stop = False

while not stop:
    if is_prime(i):
        i+=2
        continue
    j = 1

    sq_term = 2 * j **2

    while sq_term <= i:

        sq_term = 2 * j ** 2
        if is_prime(i-sq_term):
            break

        j+=1
    if sq_term >= i:
        print('i: ', i)
        stop = True
    i = i+2


