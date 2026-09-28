#todo: Задан шаблон config_default.txt, где каждому в текстовом файле параметру
# нужно сопоставить данные для подстановки.

# Содержимое файла config_default.txt
# Конфигурация приложения.
# app_name    = ?
# version     = ?
# debug       = ?

# Настройки базы данных
# db_host     = ?
# db_port     = ?
# db_name     = ?
# db_user     = ?
# db_password = ?

# Настройки API
# api_key     = ?
# api_secret  = ?
# base_url    = ?

# Пути
# log_file    = ?
# data_dir    = ?
# temp_dir    = ?


# Данные для подстановки
config_values = {
    'app_name': 'NextGen',
    'version': '1.0.0',
    'debug':  True,
    'db_host': 'localhost',
    'db_port': 5432,
    'db_name': 'my_database',
    'db_user': 'admin',
    'db_password': 'secret123',
    'api_key': 'ak_123456789',
    'api_secret': 'sk_987654321',
    'base_url': 'https://api.example.com',
    'log_file': '/var/log/app.log',
    'data_dir': '/opt/app/data',
    'temp_dir': '/tmp/app',
    'max_workers': 10,
    'timeout': 30,
    'retry_attempts': 3
}

# В итоге вместо "?" должны подставиться значения и получиться файл config.txt:

# Конфигурация приложения
# app_name    =  "NextGen"
# version     =  '1.0.0'
# debug       =  True

# Настройки базы данных
# db_host     =  5432
# .....

FILE_NAME_DEFAULT = 'config_default.txt'
FILE_NAME = 'config.txt'

with open(FILE_NAME_DEFAULT, 'r', encoding='utf-8') as file:
    raw_lines = file.readlines()

replacer = lambda l: l.replace('\n', '')
lines = list(map(replacer, raw_lines))

with open(FILE_NAME, 'w') as file:
    file.close()

import re

with open(FILE_NAME, 'a', encoding='utf-8') as file:
    def write_line_as_is(line: str) -> None:
        file.write(f"{line}\n")

    def write_line_with_new_value(line: str, new_value: any) -> None:
        stringified_value = f'"{new_value}"' if type(new_value).__name__=='str' else f'{new_value}'
        new_line = re.sub(r"=.*$", f"= {stringified_value}", line)
        file.write(f"{new_line}\n")

    for line in lines:
        is_empty = bool(re.match(r"^\s*$", line))
        is_comment = bool(re.match(r"^\s*#", line))
        is_equality = bool(re.match(r"^\s*\S+\s*=", line))
        if is_empty or is_comment or (not is_equality):
            write_line_as_is(line)
            continue
        raw_key = re.match(r"^\s*(\S+)\s*=", line).groups()[0]
        if not(raw_key in config_values):
            write_line_as_is(line)
            continue
        write_line_with_new_value(line, config_values[raw_key])

    file.close()
        


