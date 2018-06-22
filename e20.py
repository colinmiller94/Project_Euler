

fac_dic = {}
def factorial(n):
    if n in fac_dic:
        return fac_dic[n]
    elif n == 0 or n == 1:
        res = 1
        fac_dic[n] = res
        return res
    else:
        res = n * factorial(n-1)
        fac_dic[n] = res
        return res

total = 0
for digit in str(factorial(100)):
    total += int(digit)

print(total)