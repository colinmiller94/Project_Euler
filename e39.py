
def is_triangle(a,b,c):
    if a + b > c:
        if a + c > b:
            if b + c > a:
                return True
    return False


def get_solutions(n):
    solutions = []
    for a in range(1, int(n/2)):
        for b in range(1, n-a):
            c = (a**2 + b **2) ** (1/2)
            if c == int(c):
                c= int(c)
                if a + b + c == n:
                    if is_triangle(a,b,c):
                        solutions.append(sorted([a,b,c]))
    solutions = sorted(solutions)
    i = len(solutions) - 1

    while i > 0:

        if solutions[i - 1] == solutions[i]:
            del solutions[i]
        i -= 1
    return len(solutions)


max = (0 , 0)
for i in range(1,1001):
    print(i)
    res = get_solutions(i)
    if res > max[0]:
        max = (res , i)

print(max)