string = ""

for i in range(1, 10**6+1):
    string += str(i)
print(string)
product = 1

for i in range(0,7):
    index = 10 ** i  - 1
    print(index)
    product*= int(string[index])

print(product)