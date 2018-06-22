def is_palindrome(string):
    if string == string[::-1]:
        return True
    return False


total = 0
for i in range(1,10** 6 + 1):
    print(i)
    if is_palindrome(str(i)) and is_palindrome(bin(i)[2:]):
        total += i

print(total)