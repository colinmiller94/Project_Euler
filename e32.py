
def factors(n):
    lst = []
    i = 1
    while i**2 <= n:
        if n%i == 0:
            lst.append((i, n//i))
        i +=1

    return lst



def is_ninepan(n):
    for tup in factors(n):
        string = str(n) + str(tup[0]) + str(tup[1])
        if sorted([i for i in string]) == ['1','2','3','4','5','6','7','8','9']:
            return True


total = 0

for i in range(1, 10**6):
    if is_ninepan(i):
        total+= i

print(total)