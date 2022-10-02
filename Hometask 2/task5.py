# 5. ** Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

from random import random, randrange, sample


number = int(input('enter number: '))
main_list = []
for i in range(number):
    main_list.append(i)
print(main_list)
mix_list = sample(main_list, len(main_list))
print(mix_list)
