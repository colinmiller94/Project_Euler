

list = range(1,21)

i = 22

def is_div(num):
    for number in list:
        if num % number != 0:
            return 'n'

while 1 == 1:
    if is_div(i) != 'n':
        print(i)
        break
    else:
        i = i +1