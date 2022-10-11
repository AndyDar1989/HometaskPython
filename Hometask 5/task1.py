# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in Number of words: 10
# out  авб абв бав абв вба бав вба абв абв абв
#      авб бав вба бав вба

from random import choices, sample


def fill_list(num: int, chr):
    if num < 1:
        return -1
    else:
        word_list = [''.join(sample(chr, 3)) for _ in range(num)]
        return word_list


def del_word(some_list: list, word):
    new_list = []
    for i in range(len(some_list)):
        if some_list[i] != word:
            new_list.append(some_list[i])
    return (' '.join(map(str, new_list)))


n = int(input('Enter number: '))
if n < 1:
    print('incorrect value')
else:
    my_list = fill_list(n, 'абв')
    print(' '.join(my_list))
    print(del_word(my_list, 'абв'))
