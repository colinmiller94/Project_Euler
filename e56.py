
max = 0

for a in range(1,100):
    for b in range(1,100):
        power = a**b
        total = sum([int(i) for i in str(power)])
        if total > max:
            max = total

print(max)