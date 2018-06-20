import math

numlist = list(range(1,101))
#print(numlist)


sumsq = 0

for num in numlist:
    #print(num**2)
    sumsq += num **2

sqsum = sum(numlist) ** 2

print(sqsum)
print(sumsq)

dif = sqsum -sumsq

print(dif)