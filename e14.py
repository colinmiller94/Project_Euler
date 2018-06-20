def iterate(n):
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n/2
        else:
            n= 3*n + 1
        count += 1
    return count


longest = 0

print(iterate(13))


i = 1
while i < 10**6:
    if iterate(i) > longest:
        longest = iterate(i)
        print(longest)
        print(i)
    i = i + 1