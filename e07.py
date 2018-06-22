def is_prime(num):
    if num < 2:
        return 'n'
    if num == 2:
        return 'y'
    if num % 2 == 0:
        return 'n'

    count = 3
    while count ** 2 <= num:
        if num % count == 0:
            return 'n'
        else:
            count += 2

    return 'y'

print(is_prime(29))

prime_count = 0
i = 0

while prime_count < 10001:
    if is_prime(i) == 'y':
        prime_count += 1
        print(i)

    i +=1