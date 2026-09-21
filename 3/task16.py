# todo: База данных пользователя.
# Задан массив объектов пользователя

users = [
    {'login': 'Piter', 'age': 23, 'group': "admin"},
    {'login': 'Ivan', 'age': 10, 'group': "guest"},
    {'login': 'Dasha', 'age': 30, 'group': "master"},
    {'login': 'Fedor', 'age': 13, 'group': "guest"},
]

# Написать фильтр который будет выводить отсортированные объекты по возрасту(больше введеного)
# ,первой букве логина, и заданной группе.

# Сперва вводится тип сортировки:
# 1. По возрасту
# 2. По первой букве
# 3. По группе

# тип сортировки: 1

# Затем сообщение для ввода
# Введите критерии поиска: 16

# Результат:
# Пользователь: 'Piter' возраст 23 года , группа  "admin"
# Пользователь: 'Dasha' возраст 30 лет , группа  "master"

POLITICS = {
    1: {
        'criterio_name': 'По возрасту',
        'prompt': 'Возраст более:',
        'fn': lambda user, criterio1: user['age'] > float(criterio1)
    },
    2: {
        'criterio_name': 'По первой букве',
        'prompt': 'Первая буква логина:',
        'fn': lambda user, criterio: user['login'][0].upper() == criterio.upper()
    },
    3: {
        'criterio_name': 'По группе',
        'prompt': 'Принадлежность к группе:',
        'fn': lambda user, criterio: user['group'] == criterio
    },
}

sort_type = int(input(f"""
    Выберите тип сортировки:
    1. По возрасту
    2. По первой букве
    3. По группе
"""))

politic = POLITICS[sort_type]

crit = input(politic['prompt'])

fn = lambda user: politic['fn'](user, crit)

filtered = list(filter(fn, users))

print('Результат:')
for user in filtered:
    print(f"Пользователь: '{user['login']}' возраст {user['age']} года, группа \"{user['group']}\"")
