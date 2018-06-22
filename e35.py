
def is_prime(n):
    if n == 2:
        return True
    i = 2
    while i**2 <= n:
        if n%i == 0:
            return False
        i = i+1

    return True


def circle(n):
    nlist= []
    n = str(n)

    n1 = n

    n = n[1:] +n[0]
    nlist.append(int(n))
    while n != n1:
        n = n[1:] + n[0]
        nlist.append(int(n))
    return nlist

def is_circle(lst):
    for num in lst:
        if not is_prime(num):
            return False
    return True


count = 0

for i in range(2,10**6 + 1):
    print(i)
    if is_prime(i):
        if is_circle(circle(i)):
            count +=1

print(count)

