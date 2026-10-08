# Инкапсуляция и property
# todo: Класс "Пользователь" (Валидация email)
# Создайте класс User. У него должны быть свойства email и password.
# При установке email проверяйте, что строка содержит символ @ (простая валидация).
# При установке пароля, храните не сам пароль, а его хеш (для простоты можно использовать hash()).
# Сделайте метод check_password(password), который проверяет, соответствует ли хеш переданного
# пароля сохраненному хешу.

class User:
    __password_hash: int
    __email: str

    def __init__(self, email: str, password: str = ''):
        self.email = email
        self.password = password

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        if not '@' in email:
            raise TypeError("Email must include an `@` symbol")
        self.__email = email

    @property
    def password(self):
        raise AttributeError("User passwords are never stored and cannot be read.")
    @password.setter
    def password(self, password: str):
        self.__password_hash = hash(password)

    def check_password(self, password: str):
        return hash(password) == self.__password_hash
        

# Пример использования
user = User("test@example.com", "secret")
print(user.email)  # test@example.com
# print(user.password) # AttributeError
print(user.check_password("secret"))  # True
print(user.check_password("wrong"))   # False