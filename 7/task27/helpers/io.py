
# Цитата: В модуль io.py разместите ранее написаный logger
# Не ясно, о каком логгере идёт речь
# Пишу произвольный:

import datetime

def logger(msg: str):
    now = datetime.datetime.now()
    print(f"{now}: {msg}")