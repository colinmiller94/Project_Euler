def is_lychrel(n):
    count = 0

    while count < 50:
        n+= int(str(n)[::-1])
        if str(n) == str(n)[::-1]:
            return False
        count+= 1

    return True

total = 0

for i in range(1,10000):
    print(i)
    if is_lychrel(i):
        total+=1

print(total)
    