# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

A = []
A_x = float(input('Введите значение Х для точки А: '))
A_y = float(input('Введите значение Y для точки А: '))
A.append(A_x)
A.append(A_y)

B = []
B_x = float(input('Введите значение Х для точки B: '))
B_y = float(input('Введите значение Y для точки В: '))
B.append(B_x)
B.append(B_y)

print(f'Координаты точки A {A}')
print(f'Координаты точки В {B}')

Distance = (((B[0] - A[0]) ** 2 + (B[1] - A[1]) ** 2) ** (0.5))
print(Distance)
