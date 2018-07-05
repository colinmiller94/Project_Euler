def is_pent(n):
    quad = (1 + (1+24 * n)**(1/2))/6
    if quad == int(quad):
        return True
    return False



stop = False

i = 1

while not stop:
    i+=1
    pni = i*(3*i-1)/2

    j = i-1

    while j > 0:
        pnj = j*(3*j-1)/2
        if is_pent(pni+pnj) and is_pent(pni-pnj):
            print('D: ',pni - pnj)
            stop = True
            break
        j -=1


            