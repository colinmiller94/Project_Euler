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

count = 0
i = 0
while i < 2*10**6:
    if is_prime(i) == 'y':
        count += i
    print(i)
    i += 1

print(count)
