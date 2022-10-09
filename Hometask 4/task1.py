# 1. Вычислить число c заданной точностью d
# in Enter a real number: 9    Enter the required accuracy '0.0001': 0.000001
# out  9.000000

from decimal import Decimal


def accur_by_request(num: float, accur: float):
    number = Decimal(f'{num}')
    number = number.quantize(Decimal(f'{accur}'))
    print(number)


n = float(input('Enter a real number: '))
ac = float(input('Enter the required accuracy "0.0001": '))
accur_by_request(n, ac)
