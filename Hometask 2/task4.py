# * 4. Напишите программу, которая принимает на вход 2 числа. Задайте список из N элементов,
# заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях(не индексах).
# Position one: 1
# Position two: 3
# Number of elements: 5
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 15

pos_one = int(input('enter position 1: '))
pos_two = int(input('enter position 2: '))
elem = int(input('enter number of elements: '))
length = elem*2+1
if 1 <= pos_one <= length and 1 <= pos_two <= length:
    index_1 = pos_one-1
    index_2 = pos_two-1
    new_list = []
    for i in range(-elem, elem+1):
        new_list.append(i)
    print(new_list)
    mult = new_list[index_1]*new_list[index_2]
    print(mult)
else:
    print('incorrect position value')
