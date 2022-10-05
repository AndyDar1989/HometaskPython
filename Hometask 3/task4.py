# 4.* Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов.
# in  5
# out [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76

import random


def random_list(min, max, count):
    new_list = []
    for i in range(count):
        value = round(random.uniform(min, max), 2)
        new_list.append(value)
    return new_list


def diff_min_max(new_list: list):
    min = 0.99
    max = 0.00
    for i in range(len(new_list)):
        new_list[i] = round((new_list[i] % 1), 2)
        if new_list[i] < min:
            min = new_list[i]
        elif new_list[i] > max:
            max = new_list[i]
    diff = round((max-min), 2)
    print(f'Min: {min}, Max: {max}. Difference: {diff}')


c = int(input('enter count of numbers:'))
my_list = random_list(0.0, 10.0, c)
print(my_list)
diff_min_max(my_list)
