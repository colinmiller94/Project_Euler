

list1= []

for i in range(2,101):
    for j in range(2,101):
        res = i ** j
        if res not in list1:
            list1.append(res)


print(len(list1))

