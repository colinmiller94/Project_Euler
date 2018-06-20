

def is_abund(num):
    total = 0
    for i in range(1,int(num/2) + 1):
        if num%i == 0:
            total +=i
    return total
    if total > num:
        return True
    return False

print(is_abund(28))
for i in range(1,10):
    print(i)



lst = []
for i in range(1, 28123):
    if is_abund(i):
        lst.append(i)

total = 0

for i in range(1, 28123):
    for j in range(int(i/2),i+1):
        if j in lst:
            if i - j in lst:
                two_abund = True
            else:
                two_abund = False
        else:
            two_abund = False
    if not two_abund:
        total += i

print(total)