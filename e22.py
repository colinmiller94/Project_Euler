from string import ascii_uppercase



with open('p022_names.txt') as f:
    names = f.read().split(',')
    names.sort()


def score(word):
    return sum(ord(letter) - 64 for letter in word)

total = 0

for i in range(len(names)):
    #print(names[i].strip('"'))
    total += score(names[i].strip('"')) * (i+1)


print(total)