#todo: Выведите все строки данного файла в обратном порядке, допишите их в этот же файл.
# Для этого считайте список всех строк при помощи метода readlines().

#Содержимое файла inverted_sort.txt
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.

# Результат
# Complex is better than complicated.
# Simple is better than complex.
# Explicit is better than implicit.
# Beautiful is better than ugly.

FILE_NAME = 'inverted_sort.txt'

with open(FILE_NAME, 'r', encoding='utf-8') as file:
    raw_lines = file.readlines()
    file.close()

replacer = lambda l: l.replace('\n', '')
lines = list(map(replacer, raw_lines))
lines.reverse()

with open(FILE_NAME, 'a', encoding='utf-8') as file:
    for line in lines:
        print(line)
        file.write(f"\n{line}")
    file.close()