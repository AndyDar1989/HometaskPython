#1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
# является ли этот день выходным.
#*Пример:*
#- 6 -> да
#- 7 -> да
#- 1 -> нет

day = int(input('enter number: '))
if 1<=day<=5:
    print('no, its workday')
elif day==6 or day==7:
    print('yes, its holiday!')
else:    
    print('incorrect value')    