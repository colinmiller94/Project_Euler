from collections import Counter


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


def is_permutation(a,b):
    return len(a) == len(b) and Counter(a) == Counter(b)


for i in range(1000, 10000):
    if is_prime(i):
        for j in range(i+1,int((10000)-i/2)):
            if is_prime(j):
                k = 2*j - i
                if is_prime(k):
                    if k-j == j-i:
                        if is_permutation(str(i),str(j)):
                            if is_permutation(str(i),str(k)):
                                print(i,j,k)
