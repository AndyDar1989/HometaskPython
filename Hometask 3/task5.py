# 5. ** Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.
# Негафибоначчи

# in 8
# out -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21

def neg_fib(num):
    new_list = [1, 0, 1]
    if num == 1:
        return new_list
    else:
        f1 = 0
        f2 = 1
        f1_neg = 0
        f2_neg = 1
        for i in range(num-1):
            f_sum = f1+f2
            f1 = f2
            f2 = f_sum
            f_sum_neg = f1_neg-f2_neg
            f1_neg = f2_neg
            f2_neg = f_sum_neg
            new_list.insert(0, f_sum_neg)
            new_list.append(f_sum)
    return new_list


n = int(input('enter number:'))
print(neg_fib(n))
