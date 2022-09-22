# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#*Пример:*
#- A (3,6); B (2,1) -> 5,09
#- A (7,-5); B (1,-1) -> 7,21

xA = int(input('enter x-value for A: '))
yA = int(input('enter y-value for A: '))
xB = int(input('enter x-value for B: '))
yB = int(input('enter y-value for B: '))

distance = ((xB-xA)**2+(yB-yA)**2)**0.5
print(round(distance, 2))