def factors(num):
    #only works greater than 4
    ct = 2
    if num % 2 == 0:
        ct +=2
    for i in range(3,int(num/2)):
        if num% i == 0:
            ct += 1
    return ct




def triangles(num):
    sum = 0
    for i in range(num+1):
        sum+=i
    return sum

i =1
cont =  True
while cont == True:

    tri = triangles(i)
    fac = factors(tri)


    if fac > 500:
        cont == False
        print(tri)
        print(fac)
    else:
        i+= 1
        print(tri)
        print(fac)