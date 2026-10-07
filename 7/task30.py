#todo: Напишите лямбду функцию которая возвращает максимальное число
# из 2 переданных чисел
get_max = lambda x, y: max(x, y)
print(
    get_max(2, 9.56)
)


#todo: Для каждого значения из списка mass получите
# список проверок(True или False) вхождений значений в диапазон от 1 до 130
mass = [122, 23, 1425, 23, 768, 4, 67, 998, 4, 6, 867]
print(
    [1 <= x <= 130 for x in mass]
)


#todo: Отсортируйте список с помощью функции filter()
# и получите итоговый список только нечетных значений
list_ = [ 10, 11, 14, 25, 33, 36, 100, 101 ]
# Отсортируйте или отфильтруйте?
# Фильтрация:
print(
    list(filter( lambda v:  v % 2,  list_ ))
)


#todo: Отсортируйте список по расширению ".mp3"
files = ['file.txt', 'file2.mp3', 'file.pdf', 'file3.mp3', '.mp3le.doc']
# Отсортируйте или отфильтруйте?
# Фильтрация:
import re
print(
    list(
        filter(
            lambda file: file.endswith('.mp3'),
            files
        )
    )
)
# Сортировка:
sorted = list(files)
sorted.sort(key=lambda file: file.endswith('.mp3'), reverse=True)
print(sorted)


