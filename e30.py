
def sum_fifth_digits(n):
    n = str(n)
    total = 0
    for i in n:
        total += int(i)**5
    return total

print(sum_fifth_digits(1300))



total = 0
for i in range(2,10**6 +1):
    if i == sum_fifth_digits(i):
        total += i

print(total)
