

prime_dic = {}

def is_prime(n):
    if n in prime_dic:
        return prime_dic[n]
    if n == 2:
        prime_dic[n] = True
        return True
    i = 2
    while i**2 <= n:
        if n%i ==0:
            prime_dic[n] = False
            return False
        i+=1

    prime_dic[n] = True
    return True

def get_factors(n):
    if is_prime(n):
        return [n]

    factors = []
    while not is_prime(n):
        i = 2
        while i ** 2 <= n:
            if n % i == 0 and is_prime(i):
                n = n // i
                factors.append(i)
                factors.append(n)

            i = i+1

    factors = [factor for factor in factors if is_prime(factor)]

    return factors

def unique_factors(n):
    lst = []
    factors = get_factors(n)
    for i in factors:
        if i not in lst:
            lst.append(i)
    return len(lst)



lst = []
i = 0
stop = False

while not stop:
    lst.append(unique_factors(i))
    if len(lst) < 4:
        i = i + 1
        continue
    if lst[i] == 4 and lst[i-1] == 4 and lst[i-2] == 4 and lst[i-3] == 4:
        print(i-3)
        stop = True
    i = i +1



