

def is_triangle(n):
    tri = (-1 + (1+ 8*n)**(1/2))/2
    return tri == int(tri)

def score_word(word):
    score = 0
    for char in word.upper():
        char = ord(char)
        if char > 64 and char < 91:
            score+= char - 64

    return score

total = 0

with open('words.txt','r') as f:
    for line in f:
        for word in line.split("\",\""):
            if is_triangle(score_word(word)):
                total +=1

print(total)
