import itertools

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

def gen_combos(length):
    num_str = ""
    i = 1
    while i <= length:
        num_str += str(i)
        i +=1

    iter_list = list(itertools.permutations(num_str))

    new_list = [int(''.join(str(elem) for elem in tup)) for tup in iter_list]
    return new_list

length = 1
max = 0

while length < 10:
    num_lst = gen_combos(length)
    for num in num_lst:
        if is_prime(num):
            if num > max:
                max = num
    length += 1

print(max)
