def factorial(n):
    if n == 0:
        return 1
    x = n
    while (n-1) > 0:
        x *= (n-1)
        n = n -1
    return x

def fact_digits(n):
    total = 0
    for digit in str(n):
        total += factorial(int(digit))
    return total

total = 0
for i in range(3, 10000000):
    dig_fact = fact_digits(i)
    if i == dig_fact:
        print(i, dig_fact)
        total += i

print(total)