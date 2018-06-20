
fib_dict ={}

def fibonacci(n):
    if n in fib_dict:
        return fib_dict[n]
    if n == 1:
        res =1
    elif n == 2:
        res = 1
    else:
        res = fibonacci(n-1) + fibonacci(n-2)
    fib_dict[n] = res
    return res

i = 1

while fibonacci(i) < 10**999:
    #print fibonacci(i)
    i +=1
print(fibonacci(i))
print i