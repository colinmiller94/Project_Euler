i = 999
j = 999

largest = 0

def is_pdrome(num):
    if str(num) == str(num)[::-1]:
        return 'y'




while i > 0:
    while j > 0:
        #print(i,j)
        product = i * j
        if is_pdrome(product) == 'y' and product > largest:
            largest = product
            print(i, j)
        j = j - 1
    j = 999
    i = i - 1


print(largest)
