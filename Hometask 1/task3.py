#3. Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
#*Пример:*
#- x=34; y=-30 -> 4
#- x=2; y=4-> 1
#- x=-34; y=-30 -> 3

x = int(input('enter X-coordinate: '))
y = int(input('enter Y-coordinate: '))
if x>0 and y>0:
    print('first quarter')
elif x>0 and y<0:
    print('second quarter')
elif x<0 and y<0:
    print('third quarter')
elif x<0 and y>0:
    print('fourth quarter')
elif x==0 and y !=0:
    print('Y-axe')
elif y==0 and x !=0:
    print('X-axe')
elif x==0 and y==0 :
    print('zero point')            
