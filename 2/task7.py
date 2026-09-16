# todo: Даны три точки A , B , C на числовой оси. Найти длины отрезков AC и BC и их сумму.
# Примечание: все точки получаем через функцию input().

import math

points = [None, None, None]
names = ('A', 'B', 'C')
tasks = ('AC', 'BC')

for idx, point in enumerate(points):
    points[idx] = float(input(f"Введите абсциссу точки {names[idx]}: "))

summ = 0

for task in tasks:
    result = 0
    for idx, point_name in enumerate(task):
        name_idx = names.index(point_name)
        result = points[name_idx] if idx == 0 else (result - points[name_idx])
    result = math.fabs(result)
    summ += result
    print(f"Длина отрезка {task} равна {result}")

print(f"Сумма длин отрезков равна {summ}")
