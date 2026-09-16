# todo: Проверить истинность высказывания:
#  "Данное четырехзначное число читается одинаково слева направо и справа налево".

value = int(input("Введите целое число: "))

value_arr = list(str(value))

inverted = list(value_arr)
inverted.reverse()


def print_fault():
    print('Нет. Это число не читается наоборот так же, как и напрямую')


def print_success():
    print('Да. Это число читается наоборот так же, как и напрямую')


if len(value_arr) != len(inverted):
    print_fault()
    exit(0)

for idx, digit in enumerate(value_arr):
    if digit != inverted[idx]:
        print_fault()
        exit(0)

print_success()
