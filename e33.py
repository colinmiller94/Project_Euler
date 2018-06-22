
numerator = 1
denominator = 1


for i in range(10,100):
    for j in range(i+1,100):

        i1 = float(str(i)[0])
        i2 = float(str(i)[1])
        j1 = float(str(j)[0])
        j2 = float(str(j)[1])

        if i2 == 0 and j2 == 0:
            continue



        if i1 == j2 and j1 != 0:
            if i/j == i2/j1:
                numerator *=i
                denominator *= j
                print(i,j,i/j)
        elif i2 == j1 and j2 !=0:
            if i/j == i1/j2:
                numerator *= i
                denominator *= j
                print(i,j,i/j)


def simplify(x,y):
    i = 2
    while i <= min([x,y]):
        if x%i == 0 and y %i == 0:
            x = x//i
            y = y//i
            i = 2
            simplify(x,y)
        i+= 1

    return x,y

print(simplify(numerator,denominator))