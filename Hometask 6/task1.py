# 1. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента. Use comprehension.
# in  9

# out  [15, 16, 2, 3, 1, 7, 5, 4, 10]
#      [16, 3, 7, 10]


from random import sample


def fill_list(count: int):
    rand_list = sample(range(0, 20), count)
    return rand_list


def find_elem(my_list: list):
    new_list = [my_list[x]
                for x in range(1, len(my_list)) if my_list[x] > my_list[x-1]]
    return new_list


some_list = fill_list(9)
print(some_list)
print(find_elem(some_list))
