#todo Задача 1. Чтение матрицы, load_matrix(filename)
# Дан файл, содержащий таблицу целых чисел вида
# (в каждой строке через пробел записаны числа)

# 11 12 13 14 15 16
# 21 22 23 24 25 26
# 31 32 33 34 35 36


# Требуется написать функцию load_matrix(filename) которая загружает эту таблицу из файла.
# Если в каждой строке находится одинаковое количество чисел, функция возвращает список списков целых чисел.
# В противном случае возвращает False.

# Задачу следует решить с использованием списковых включений, циклы использовать НЕЛЬЗЯ!

from typing import List, Set
import re


def is_integer_word(word: str) -> bool:
    return bool(re.match('^[\\+-]?\\d+$', word))


def load_matrix(filename: str) -> List[List[int]] | False:
    with open(filename) as file:
        result: List[List[int]] = [
            [
                int(word)
                for word in raw_line.split()
                if is_integer_word(word)
            ]
            for raw_line in file
        ]
        lengths: Set[int] = set(
            [len(line) for line in result]
        )
        is_regular: bool = len(lengths) == 1
        return is_regular and result


print(
    load_matrix('task26.txt')
) 
