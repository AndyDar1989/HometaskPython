# 2. Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.
# in   54
# out  [2, 3, 3, 3]

def prime_mult(num):
    new_list = []
    for i in range(2, num):
        while num % i == 0 and num >= 0:
            new_list.append(i)
            num /= i
    return new_list


n = int(input('Enter a natural number: '))
print(prime_mult(n))
