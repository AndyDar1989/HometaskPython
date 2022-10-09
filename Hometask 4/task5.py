# 5. ** Даны два файла, в каждом из которых находится запись многочленов.
# Задача - сформировать файл, содержащий сумму многочленов.
# in
# "poly.txt"
# "poly_2.txt"

# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 + 2*x^2 + 2*x^1 + 2 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 + 3*x^3 - 4*x^2 - 2*x^1 - 4 = 0
# 4*x^2 - 4 + 3*x^6 - 4*x^5 - 4*x^4 - 4*x^3 + 3*x^2 - 2*x^1 - 0 = 0

def poly_sum(file_1, file_2):
    with open(file_1, 'r', encoding='utf_8') as my_file1,\
        open(file_2, 'r', encoding='utf_8') as my_file2,\
            open('file_3.txt', 'w', encoding='utf_8') as my_file3:
        first_file = my_file1.readlines()
        sec_file = my_file2.readlines()
        if len(first_file) == len(sec_file):
            for i, j in enumerate(first_file):
                my_file3.write(f'{j[:-5]}+{sec_file[i]}')
        else:
            print('Merger is not possible: different number of lines')


poly_sum('file.txt', 'file2.txt')
