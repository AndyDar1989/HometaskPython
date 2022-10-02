# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# Для n = 6: [2, 2, 2, 2, 2, 3] -> 13

n = int(input('enter number: '))
sum = 0
new_list = []
for i in range(n):
    n = round((1+1/n)**n)
    new_list.append(n)
    sum += n
new_list.reverse()
print(new_list, '->', sum)
