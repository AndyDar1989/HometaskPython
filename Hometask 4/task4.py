# 4.* Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (от 0 до 10) многочлена, записать в файл полученный многочлен не менее 3-х раз.
# in 9 5 3

# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0
from random import choices, choice


def poly_coef(k):
    c = choices(range(0, 10), k=10)
    with open('file.txt', 'a', encoding='utf_8') as my_file:
        i = k
        while i > 0:
            if c[i] > 0:
                my_file.write(f"{c[i]}*x^{i}{choice('+-')}")
                i = i-1
            elif c[i] == 0:
                i = i-1
        my_file.write(f'{c[i]}=0\n')


for t in range(3):
    k = int(input('enter number: '))
    poly_coef(k)
