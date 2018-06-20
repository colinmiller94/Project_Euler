def main(n):
    prob = 1

    count = n

    tcount = n * 2
    while count > 0:
        prob *= count/tcount
        count -=1
        tcount -=1

    return 1/prob

print(main(20))
