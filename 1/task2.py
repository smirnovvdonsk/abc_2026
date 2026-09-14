# todo: Преобразуйте переменную age и foo в число
age = "23"
foo = "23abc"
age = int(age)
# age = float(age)
# foo = int(foo) # Очень бедный API

# Преобразуйте переменную age в Boolean
age = "123abc"
age = bool(age)


# Преобразуйте переменную flag в Boolean
flag = 1
flag = bool(flag)
flag = not not flag

# Преобразуйте значение в Boolean
str_one = "Privet"
str_two = ""

str_one = bool(str_one)
str_two = not not str_two
#
# Преобразуйте значение 0 и 1 в Boolean

bool(0)
not not 1

# Преобразуйте False в строку

str(False)