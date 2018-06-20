

def pyth(a,b,c):
    if a**2 + b**2 == c**2:
        return True
    return False

nlist = list(range(0,1000))

for num in nlist:
    for i in range(num, 1000 - num):
        for j in range(i, 1000 - i):
            if num + i + j == 1000:
                if pyth(num, i, j):
                    print(num, i ,j)
                    print(num * i * j)
                    exit(1)