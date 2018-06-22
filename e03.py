import math

#number = 600851475143
number = 13195
i = 1




largest = 0
while i < math.sqrt(number) :

    if number % i == 0:
        prime = 'y'
        for j in range(2,i):
            if i % j == 0:
                prime = 'n'

        if prime == 'y' and i > largest:
            largest = i

    i = i+1

print(largest)