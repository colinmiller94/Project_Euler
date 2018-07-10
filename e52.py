from collections import Counter
def is_permutation(a,b):
    return len(a) == len(b) and Counter(a) == Counter(b)

stop = False
i = 1
while not stop:
    if is_permutation(str(i),str(2*i)):
        if is_permutation(str(i), str(3 * i)):
            if is_permutation(str(i), str(4 * i)):
                if is_permutation(str(i), str(5 * i)):
                    if is_permutation(str(i), str(6 * i)):
                        print("i: ",i)
                        stop = True

    i += 1