# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.
# in  88
# out  1011000

def convert_to_bin(number):
    bin_list=[]
    while number:
        item = number%2
        bin_list.append(item)
        number = number//2
    bin_list.reverse()
    for i in range(len(bin_list)):
        print (f'{bin_list[i]}', end='')
    
    
n = int(input('enter positive number: '))
convert_to_bin(n)