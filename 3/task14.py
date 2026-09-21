# todo: Дан массив размера N. Найти минимальное растояние между одинаковыми значениями в массиве и вывести их индексы.
# Одинаковых значение может быть два и более !

# Для числа 1 минимальное растояние в массиве по индексам: 0 и 7
# Для числа 2 минимальное растояние в массиве по индексам: 6 и 9
# Для числа 17 нет минимального растояния т.к элемент в массиве один.


mass = [1, 2, 17, 54, 30, 89, 2, 1, 6, 2]


def get_distances(array_of_indice):
    result = []
    for i, index in enumerate(array_of_indice):
        if i < 1:
            continue
        result.append(index - array_of_indice[i - 1])
    return tuple(result)


dictionary = {}

for idx, value in enumerate(mass):
    if value not in dictionary:
        dictionary[value] = []
    dictionary[value].append(idx)

deduped = set(mass)

for value in deduped:
    indices = dictionary[value]
    if len(indices) <= 1:
        print(f"Для числа {value} нет минимального растояния, т.к. элемент в массиве один")
        continue
    min_distance = min(get_distances(dictionary[value]))
    indices_str = ", ".join(map(lambda n: str(n), dictionary[value]))
    print(f"Для числа {value} минимальное растояние в массиве равно {min_distance} по индексам: {indices_str}")
