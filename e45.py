def is_pent(n):
    quad = (1 + (1+24 * n)**(1/2))/6
    if quad == int(quad):
        return True
    return False

def is_hex(n):
    quad = (1 + (1+ 8 * n)**(1/2))/4
    if quad == int(quad):
        return True
    return False


stop = False

i = 286
while not stop:
    tn = i * (i+1) / 2
    if is_hex(tn):
        if is_pent(tn):
            stop = True
            print('Tn: ',tn)

    i+=1


print(is_hex(7906276))

