# 3. Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
# in  7
# out[4, 5, 3, 3, 4, 1, 2]
#     [5, 1, 2]

# in  -1
# out Negative value of the number of numbers! []
from collections import Counter
from random import choices


def random_list(min, max, count):
    new_list = choices(range(min, max), k=count)
    return new_list


def nonrepeat_elem(user_list: list):
    counter = Counter(user_list)
    new_list = []
    for num, count in counter.items():
        if count == 1:
            new_list.append(num)
    return new_list


n = int(input('Enter a real number: '))
if n <= 0:
    print('incorrect value of the numbers')
else:
    some_list = random_list(0, 10, n)
    print(some_list)
    print(nonrepeat_elem(some_list))
