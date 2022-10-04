# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in  4
# out  [2, 5, 8, 10]   [20, 40]

from random import sample
def random_list(min, max, count):
    new_list = sample(range(min, max), count)
    return new_list

def mult_of_pair_elem(new_list: list):
    new_list2=[]
    count = len(new_list)//2
    for i in range (count):
        mult = new_list[i]*new_list[-i-1]
        new_list2.append(mult)
    if len(new_list)%2:
        new_list2.append(new_list[count])    
    return new_list2

c = int(input('enter count of numbers:'))
my_list = random_list(0, 10, c)
print(my_list)
print(mult_of_pair_elem(my_list))
