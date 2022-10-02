# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

number = float(input('enter number: '))
pow = len(str(number))-1
count = 10**pow
sum = 0
if number >= 0:
    new_number = number*count
    while new_number:
        temp_res = new_number % 10
        sum += temp_res
        new_number //= 10
    print(round(sum))
else:
    new_number = number*count*-1
    while new_number >= 10:
        temp_res = new_number % 10
        sum += temp_res
        new_number //= 10
    sum -= new_number
    print(round(sum))
