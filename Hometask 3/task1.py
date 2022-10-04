# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётных позициях(не индексах).
# in 5
# out [10, 2, 3, 8, 9]  22

from random import sample
def random_list(min, max, count):
    new_list = sample(range(min, max), count)
    return new_list

def sum_of_elements(new_list: list):
    sum = 0
    for i in range(0, len(new_list)-1, 2):
        sum += new_list[i]
    return sum

c = int(input('enter count of numbers:'))
my_list = random_list(0, 10, c)
print(my_list)
print(sum_of_elements(my_list))
