list = [1,2]

i = 1

while list[i] < 4000000:
    list.append(list[i-1]+ list[i])
    i +=1

print(list)
sum = 0
for number in list:
    if number %2 == 0:
        sum += number

print(sum)