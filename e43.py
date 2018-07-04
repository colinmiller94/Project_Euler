import itertools
def gen_combos(length):
    num_str = ""
    i = 0
    while i <= length:
        num_str += str(i)
        i +=1

    iter_list = list(itertools.permutations(num_str))

    new_list = [''.join(str(elem) for elem in tup) for tup in iter_list if tup[0] != '0']

    return new_list

pan_numbers = gen_combos(9)

sum = 0

prime_list = [2,3,5,7,11,13,17]

for num in pan_numbers:
    i =  1
    print(num)
    while i < 8:
        if int(num[i:i+3]) %prime_list[i-1] != 0:
            break
        i += 1
    if i < 8:
        continue
    sum += int(num)

print('sum: ',sum)
