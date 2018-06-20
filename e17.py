
one_d_dic = {'0': 0,'1': 3, '2': 3,'3': 5, '4': 4,'5': 4, '6': 3,'7': 5, '8': 5, '9': 4}
teen_dic = {'10': 3, '11': 6,'12': 6, '13': 8,'14': 8, '15': 7,'16': 7, '17': 9, '18': 8, '19': 8}
ty_dic = {'2': 6,'3': 6, '4': 5,'5': 5, '6': 5,'7': 7, '8': 6, '9': 6}


def count_characters_100u(num):

    if num < 10:
        return one_d_dic[str(num)]

    elif num < 20:
        return teen_dic[str(num)]

    elif num < 100:
        return ty_dic[str(num)[0]] + one_d_dic[str(num)[1]]

def count_characters_100p(num):
    if num % 100 == 0 and num != 1000:
        return one_d_dic[str(num)[0]] + 7
    elif num == 1000:
        return 11
    else:
        return one_d_dic[str(num)[0]] + 10 + count_characters_100u(int(str(num)[1:]))

count = 0

for i in range(1,100):
    count += count_characters_100u(i)

for i in range(100,1001):
    count += count_characters_100p(i)

print(count)