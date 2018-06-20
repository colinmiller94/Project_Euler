def simplify(x,y):
    i = 2
    while i <= int(y/2) + 1:
        print i
        if x%i == 0 and y%i == 0:
            x = x/i
            y = y/i
            simplified = True
            break
        else:
            simplified = False
        i = i +1
    if simplified:
        simplify(x,y)
    else:
        return x,y

print(simplify(12,4))